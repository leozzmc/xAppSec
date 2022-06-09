#!/usr/bin/env python3
from veinmind import *
import time as timep
from lib import tools
import os
import re
import pytoml as toml
from report import *

report_list = []
instruct_set = (
    "FROM", "CMD", "RUN", "LABEL", "MAINTAINER", "EXPOSE", "ENV", "ADD", "COPY", "ENTRYPOINT",
    "VOLUME", "USER","WORKDIR","ARG", "ONBUILD", "STOPSIGNAL", "HEALTHCHECK", "SHELL")


def load_rules():
    global rules
    with open("rules.toml", encoding="utf8") as f:
        rules = toml.load(f)


@command.group()
def cli():
    global start
    start = timep.time()
    load_rules()
    


@cli.image_command()
def xapp_scan_images(image):
    """scan image abnormal history instruction"""
    image_report = None
    refs = image.reporefs()
    if len(refs) > 0:
        ref = refs[0]
    else:
        ref = image.id()
    log.info("start scan: " + ref)

    ocispec = image.ocispec_v1()
    if 'history' in ocispec.keys() and len(ocispec['history']) > 0:
        for history in ocispec['history']:
            if 'created_by' in history.keys():
                created_by = history['created_by']
                created_by_split = created_by.split("#(nop)")
                if len(created_by_split) > 1:
                    command = "#(nop)".join(created_by_split[1:])
                    command = command.lstrip()
                    command_split = command.split()
                    if len(command_split) == 2:
                        instruct = command_split[0]
                        command_content = command_split[1]
                        for r in rules["rules"]:
                            if r["instruct"] == instruct:
                                if re.match(r["match"], command_content):
                                    detail = AlertDetail()
                                    detail.history_detail = HistoryDetail(
                                                              instruction=instruct, content=command_content,
                                                              description=r["match"]
                                                          )
                                    image_report = ReportEvent(id=image.id(),
                                                          level=Level.High.value, detect_type=DetectType.Image.value,
                                                          event_type=EventType.Risk.value,
                                                          alert_type=AlertType.AbnormalHistory.value,
                                                          alert_details=[detail])
                                    report(image_report)
                                    break
                    else:
                        instruct = command_split[0]
                        command_content = " ".join(command_split[1:])
                        for r in rules["rules"]:
                            if r["instruct"] == instruct:
                                if re.match(r["match"], command_content):
                                    detail = AlertDetail()
                                    detail.history_detail = HistoryDetail(
                                                              instruction=instruct, content=command_content,
                                                              description=r["match"]
                                                          )
                                    image_report = ReportEvent(id=image.id(),
                                                          level=Level.High.value, detect_type=DetectType.Image.value,
                                                          event_type=EventType.Risk.value,
                                                          alert_type=AlertType.AbnormalHistory.value,
                                                          alert_details=[detail])
                                    report(image_report)
                                    break
                else:
                    command_split = created_by.split()
                    if command_split[0] in instruct_set:
                        for r in rules["rules"]:
                            if r["instruct"] == command_split[0]:
                                if re.match(r["match"], " ".join(command_split[1:])):
                                    detail = AlertDetail()
                                    detail.history_detail = HistoryDetail(
                                                              instruction=command_split[0],
                                                              content=" ".join(command_split[1:]),
                                                              description=r["match"]
                                                          )
                                    image_report = ReportEvent(id=image.id(),
                                                          level=Level.High.value, detect_type=DetectType.Image.value,
                                                          event_type=EventType.Risk.value,
                                                          alert_type=AlertType.AbnormalHistory.value,
                                                          alert_details=[detail])
                                    report(image_report)
                                    break
                    else:
                        for r in rules["rules"]:
                            if r["instruct"] == "RUN":
                                if re.match(r["match"], created_by):
                                    detail = AlertDetail()
                                    detail.history_detail = HistoryDetail(
                                                              instruction="RUN", content=created_by,
                                                              description=r["match"]
                                                          )
                                    image_report = ReportEvent(id=image.id(),
                                                          level=Level.High.value, detect_type=DetectType.Image.value,
                                                          event_type=EventType.Risk.value,
                                                          alert_type=AlertType.AbnormalHistory.value,
                                                          alert_details=[detail])
                                    report(image_report)
                                    break

    if image_report != None:
        report_list.append(image_report)


@cli.resultcallback()
def callback(result):
    spend_time = timep.time() - start
    print("# ================================================================================================= #")
    
    if len(report_list) > 0:
        tools.tab_print(">> \033[48;5;234m\033[38;5;202mScan Image Total:\033[0;0m " + str(len(report_list)), expandNum=128)
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mSpend Time:\033[0;0m " + spend_time.__str__() + "s",expandNum=128)   
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mUnsafe Image:\033[0;0m ", expandNum=128)
        for r in report_list:
            if len(r.alert_details) == 0:
                continue
            print(
                "+---------------------------------------------------------------------------------------------------+")
            tools.tab_print("ImageName: " + r.id, expandNum=100)
            tools.tab_print("Abnormal History Total: " + str(len(r.alert_details)), expandNum=100)
            for detail in r.alert_details:
                if detail.history_detail:
                    tools.tab_print("History: " + detail.history_detail.content, expandNum=100)
        print("+---------------------------------------------------------------------------------------------------+")
    else:
        tools.tab_print(">> \033[48;5;234m\033[38;5;202mScan Image Total:\033[0;0m " + "1", expandNum=128)
        tools.tab_print(">> \033[48;5;234m\033[38;5;202mSpend Time:\033[0;0m " + spend_time.__str__() + "s",expandNum=128)
        tools.tab_print(">> \033[48;5;234m\033[38;5;202mUnsafe Image List:\033[0;0m " + "0", expandNum=128)
        print("+---------------------------------------------------------------------------------------------------+")



if __name__ == '__main__':
    cli()

"""
Reference:

[1]https://blog.tienyulin.com/open-container-initiative-oci/
"""
