#!/usr/bin/env python3
import click
import jsonpickle
import time as timep
import os
from lib import tools
from veinmind import *
from plugins import *
from report import *
from service import *

results = []
start = 0
image_ids = []

crontabObj = crontab.crontab()
bashrcObj = bashrc.bashrc()
serviceObj = service()
sshdObj = sshd.sshd()
tcpObj = tcpwrapper.tcpwrapper()
plugin_list = [crontabObj,bashrcObj,serviceObj,sshdObj,tcpObj]

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
    
    for i in plugin_list:
        for r in i.detect(image):
            print(r)
            results.append(r)
            file_stat = image.stat(r.filepath)
            detail = AlertDetail.backdoor(backdoor_detail=BackdoorDetail(r.description, FileDetail.from_stat(r.filepath, file_stat)))
            report_event = ReportEvent(id=image.id(), level=Level.High.value,
                                    detect_type=DetectType.Image.value,
                                    event_type=EventType.Risk.value,
                                    alert_type=AlertType.Backdoor.value,
                                    alert_details=[detail])
            report(report_event)

@cli.command()
def test():
    """for testing the function call """
    for i in plugin_list:
        print(i)

@cli.resultcallback()
def callback(result, format, output):
    spend_time = timep.time() - start

    if format == "stdout":
        print("# ================================================================================================= #")
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mScan Image Total:\033[0;0m " + str(len(image_ids)))
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mSpend Time:\033[0;0m " + spend_time.__str__() + "s")
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mBackdoor Total:\033[0;0m " + str(len(results)))
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


"""
Reference Websites:
[1] https://stackabuse.com/how-to-print-colored-text-in-python/
"""

