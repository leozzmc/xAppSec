#!/bin/bash
# '''This scipt is cmd tool for onboarding xApp'''
# '''Then do the Image Security Check'''



#  Get the xApp descriptor file paths
read -p "Please provide the path to your xApp descriptor configuration file: " CONFIG_JSON
read -p "Please provide the path to your xApp descriptor schema file: " SCHEMA_JSON
echo  -e "\nxApp Descriptor Config.json Path:" ${CONFIG_JSON} 
echo  -e "xApp Descriptor Schema.json Path:" ${SCHEMA_JSON}

#  Onboard the xApp
dms_cli onboard $CONFIG_JSON $SCHEMA_JSON
sleep 2
curl -X GET http://localhost:8080/api/charts | jq .

#  Get ImageName
echo "+-----------------------------------------------+"
CONTAINER_NUM=$(cat  ${CONFIG_JSON}  | jq -c ".containers" | jq length)
declare -a IMAGE_SET=()

INDEX=0
while [ $INDEX -lt  $CONTAINER_NUM ]
do
    REGISTRY+=$(cat  ${CONFIG_JSON}  | jq -c ".containers[$INDEX].image.registry"| tr -d '"')
    REGISTRY+=$(cat  ${CONFIG_JSON}  | jq -c ".containers[$INDEX].image.name"| tr -d '"')
    REGISTRY+=$(cat  ${CONFIG_JSON}  | jq -c ".containers[$INDEX].image.tag" | tr -d '"')
    IMAGE_SET+=($REGISTRY)
	docker pull ${IMAGE_SET[$INDEX]}
    (( INDEX++ ))
done




#  ImageRegistryCheck.py
# chmod +x ~/xAppSec/Image_Security_Module/ImageRegistryCheck.py
# ../Image_Security_Module/ImageRegistryCheck.py $IMAGE_NAME

#  Backdoor_Scan.py

#  ImageHistory_Scan.py

#  Ask if want to install the xApp

#  Install the xApp (If yes)

#  Check if xApp is in "Running" State

#  Return the Kibana Service Address