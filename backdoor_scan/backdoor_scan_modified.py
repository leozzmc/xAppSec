#!/usr/bin/env python3
import click
import jsonpickle
import time as timep
import os, sys
from lib import log
from lib import tools
from veinmind import *
from plugins import *
from report import *


results = []
start = 0
image_ids = []

@command.group()
@click.option('--format', default="stdout", help="output format e.g. stdout/json")
@click.option('--output', default='.', help="output path e.g. /tmp")
def cli(format, output):
    global start
    start = timep.time()
    pass


@cli.image_command()
def xApp_scan_images(image):
    """scan image backdoor within xApp descriptor files"""
    global image_ids
    image_ids.append(image.id())
    if len(image.reporefs()) > 0:
        log.info("start scan: " + image.reporefs()[0])
    else:
        log.info("start scan: " + image.id())
    for plugin_name, plugin in register.plugin_dict.items():
        p = plugin()
        for r in p.detect(image):
            results.append(r)
            file_stat = image.stat(r.filepath)
            detail = AlertDetail.backdoor(backdoor_detail=BackdoorDetail(r.description, FileDetail.from_stat(r.filepath, file_stat)))
            report_event = ReportEvent(id=image.id(), level=Level.High.value,
                                       detect_type=DetectType.Image.value,
                                       event_type=EventType.Risk.value,
                                       alert_type=AlertType.Backdoor.value,
                                       alert_details=[detail])
            report(report_event)

@cli.resultcallback()
def callback(result, format, output):
    spend_time = timep.time() - start

    if format == "stdout":
        print("# ================================================================================================= #")
        tools.tab_print("Scan Image Total: " + str(len(image_ids)))
        tools.tab_print("Spend Time: " + spend_time.__str__() + "s")
        tools.tab_print("Backdoor Total: " + str(len(results)))
        for r in results:
            print("+---------------------------------------------------------------------------------------------------+")
            tools.tab_print("ImageName: " + r.image_ref)
            tools.tab_print("Backdoor File Path: " + r.filepath)
            tools.tab_print("Description: " + r.description)
        print("+---------------------------------------------------------------------------------------------------+")
        print("# ================================================================================================= #")

    elif format == "json":
        fpath = os.path.join(output, "report.json")
        with open(fpath, mode="w") as f:
            f.write(jsonpickle.dumps(results))


if __name__ == '__main__':
    cli()


## Origin 'Register' Class
plugin_dict = {}
plugin_name = []

def register(cls, plugin_name):
    def wrapper(plugin):
        cls.plugin_dict[plugin_name] = plugin
        return plugin
    return wrapper

## Origin 'Report' function
def report(evt, *args, **kwargs):
    if service.is_hosted():
        try:
            evt_dict = json.loads(jsonpickle.encode(evt))
            _report(evt_dict)
        except RuntimeError as e:
            log.error(e)
    else:
        log.warn(jsonpickle.encode(evt, indent=4))
