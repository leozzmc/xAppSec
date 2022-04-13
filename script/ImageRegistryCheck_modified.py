#!/usr/bin/env python3
import json
import click
import time as timep
from lib import tools
from veinmind import *

start = 0
image_ids = []
registry_List = []
decision = []



# The registry whitelist is only "nexus3.o-ran-sc.org:10002" for now.
while_List = ["nexus3.o-ran-sc.org:10002"]

@command.group()
@click.option('--format', default="stdout", help="output format e.g. stdout/json")
def cli(format):
    global start
    start = timep.time()
    pass

@cli.image_command()
def registry_check(image):
    """check the registry of image within xApp descriptor files"""
    global image_ids
    global registry_List
    global decision
    image_ids.append(image.id())
    registry_List.append(image.reporefs()[0])
    if len(image.reporefs()) > 0:
        log.info("start scan: " + image.reporefs()[0])
    else:
        log.info("start scan: " + image.id())   
    # the registry in Registry_List contain 'True', it means the registry != "nexus3.o-ran-sc.org:10002"
    for i in registry_List:
        if "nexus3.o-ran-sc.org:10002" not in i:
            decision.append(True)
        else:
            decision.append(False)


@cli.resultcallback()
def callback(result, format ):
    if format == "stdout":
        spend_time = timep.time() - start
        print("# ================================================================================================= #")
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mScan Image Total:\033[0;0m " + str(len(registry_List)),expandNum=128)
        tools.tab_print(" >> \033[48;5;234m\033[38;5;202mSpend Time:\033[0;0m " + spend_time.__str__() + "s",expandNum=128)
        for r in range(0,len(decision)):
            tools.tab_print("RegistryName: " + str(registry_List[r]),expandNum=100)
            print("+---------------------------------------------------------------------------------------------------+") 
            if decision[r] == True:
                tools.tab_print("Descriptions: " + "the image registry of this image is invalid",expandNum=100)
            else:
                tools.tab_print("Descriptions: " + "the image registry of this image is valid",expandNum=100)
        print("+---------------------------------------------------------------------------------------------------+")
        print("# ================================================================================================= #")
        pass
    elif format == "json":
        pass


if __name__ == '__main__':
    cli()




###  "Functionality" ###
#🔹 It Should eventually write to a analysis report file. It cloud be JSON format.
#🔹 Input specific registry name or scan through all image then comapre the registry name.

###  "Integration" ###
#🔹 The input shouldbe the image name
#🔹 The xAppSec.sh can extract the image registry with the xApp descriptor file.
