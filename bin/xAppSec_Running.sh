#!/bin/bash
# '''This scipt is cmd tool for onboarding xApp'''
# '''Then do the Image Security Check'''



#  Get the xApp descriptor file paths
read -p "Please provide the path to your xApp descriptor configuration file: " CONFIG_JSON
read -p "Please provide the path to your xApp descriptor schema file: " SCHEMA_JSON
echo  -e "\nxApp Descriptor Config.json Path:" ${CONFIG_JSON} 
echo  -e "xApp Descriptor Schema.json Path:" ${SCHEMA_JSON}

#  Install dms_cli(xapp_onboarder)
sleep 2
cd ~
git clone "https://gerrit.o-ran-sc.org/r/ric-plt/appmgr"
cd appmgr/xapp_orchestrater/dev/xapp_onboarder
pip3 install ./
sudo chmod 755 /usr/local/bin/dms_cli

#  Onboard the xApp
dms_cli onboard $CONFIG_JSON $SCHEMA_JSON
sleep 2
curl -X GET http://localhost:8080/api/charts | jq .

#  ImageRegistryCheck.py

#  Backdoor_Scan.py

#  ImageHistory_Scan.py

#  Ask if want to install the xApp

#  Install the xApp (If yes)

#  Check if xApp is in "Running" State

#  Return the Kibana Service Address