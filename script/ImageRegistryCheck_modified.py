#!/usr/bin/env python3
import json
import click
import time as timep
from lib import tools
from veinmind import *

start = 0
Registry_List = []
Decision = []


# The registry whitelist is only "nexus3.o-ran-sc.org:10002" for now.
While_List = ["nexus3.o-ran-sc.org:10002"]

@command.group()
def cli(format):
    global start
    start = timep.time()
    pass

# @cli.command()
# def registry_check(config_file):
#     """check the registry of image within xApp descriptor files"""
#     with open(config_file,"r") as configfile:
#         data = json.load(configfile)

#     for i in range(0, len(data['containers']) ):
#         Registry_List.append(data['containers'][i]['image']['registry'])
#         #print(Registry_List[i])
#     configfile.close()

#     for i in Registry_List:
#         if i != "nexus3.o-ran-sc.org:10002":
#             print (f"\n❎ the image registry: \"{i}\" of xApp is invalid!")

@cli.image_command()
def registry_check(image):
    """check the registry of image within xApp descriptor files"""
    global Registry_List
    global Decision
    Registry_List.append(image.id())
    if len(image.reporefs()) > 0:
        log.info("start scan: " + image.reporefs()[0])
    else:
        log.info("start scan: " + image.id())
    
    # the registry in Registry_List contain 'True', it means the registry != "nexus3.o-ran-sc.org:10002"
    for i in Registry_List:
        if i != "nexus3.o-ran-sc.org:10002":
            Decision.append(True)
        else:
            Decision.append(False)




@cli.resultcallback()
def callback( ):
    spend_time = timep.time() - start
    print("# ================================================================================================= #")
    tools.tab_print(" >> \033[48;5;234m\033[38;5;202mScan Image Total:\033[0;0m " + str(len(Registry_List)))
    tools.tab_print(" >> \033[48;5;234m\033[38;5;202mSpend Time:\033[0;0m " + spend_time.__str__() + "s")
    for r in range(0,len(Decision)):
        if Decision[r] == 'True':
            print("+---------------------------------------------------------------------------------------------------+")
            tools.tab_print("ImageName: " + Registry_List[r] )
            tools.tab_print("Descriptions: " + "the image registry of this image is invalid")
    print("+---------------------------------------------------------------------------------------------------+")
    print("# ================================================================================================= #")
    pass


if __name__ == '__main__':
    cli()


#####  Should Write to Analysis Result File ! ##########
#                                                      #
#                                                      #
#                                                      #
########################################################