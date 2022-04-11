#!/usr/bin/env python3
import json
import click
from lib import tools
from veinmind import *


Registry_List = []

# The registry whitelist is only "nexus3.o-ran-sc.org:10002" for now.
While_List = ["nexus3.o-ran-sc.org:10002"]

@command.group()
@click.option('--format', default="stdout", help="output format e.g. stdout/json")
def cli(format ):
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
def registry_check():
    pass



@cli.resultcallback()
def callback(Registry_List, format):
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
        pass
    elif format == "json":
        pass


if __name__ == '__main__':
    cli()


#####  Should Write to Analysis Result File ! ##########
#                                                      #
#                                                      #
#                                                      #
########################################################