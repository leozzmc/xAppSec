#!/usr/bin/env python3
from calendar import c
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
        if i is crontabObj:
            log.info("Start scanning Crontab backdoors...")
            for j in crontabObj.cron_list:
                log.info(f"Scanning backdoors in path {j}")
        if i is bashrcObj:
            log.info("Start scanning Bashrc backdoors..")
            for j in bashrcObj.bashrc_dirs:
                log.info(f"Scanning backdoors in path {j}")
        if i is serviceObj:
            log.info("Start scanning system service related backdoors...")
            for j in serviceObj.service_dir_list:
                log.info(f"Scanning backdoors in path {j}")
        if i is sshdObj:
            log.info("Start scanning sshd related backdoors...")
            for j in sshdObj.rootok_list:
                log.info(f"Check if any sshd symbolic link to process: {j}")
        if i is tcpObj:
            log.info("Start scanning tcp wrapper related backdoors...")
            for j in tcpObj.wrapper_config_file_list:
                log.info(f"Scanning backdoors in wrapper config file: {j}")


@cli.command()
def test():
    """for testing the function call"""
    for i in plugin_list:
        print(i)

@cli.resultcallback()
def callback(result, format, output):
    spend_time = timep.time() - start

    if format == "stdout":
        print("# ================================================================================================= #")
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mScan Image Total:\033[0;0m " + str(len(image_ids)),expandNum=128)
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mSpend Time:\033[0;0m " + spend_time.__str__() + "s",expandNum=128)
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mBackdoor Total:\033[0;0m " + str(len(results)),expandNum=128)
        for r in results:
            print("+---------------------------------------------------------------------------------------------------+")
            tools.tab_print("ImageName: " + r.image_ref,expandNum=100)
            tools.tab_print("Backdoor File Path: " + r.filepath,expandNum=100)
            tools.tab_print("Description: " + r.description,expandNum=100)
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

