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

INDEX=0
while [ $INDEX -lt  $CONTAINER_NUM ]
do
    REGISTRY=$(cat  ${CONFIG_JSON}  | jq -c ".containers[$INDEX].image.registry"| tr -d '"')
    NAME=$(cat  ${CONFIG_JSON}  | jq -c ".containers[$INDEX].image.name"| tr -d '"')
    TAG=$(cat  ${CONFIG_JSON}  | jq -c ".containers[$INDEX].image.tag" | tr -d '"')
	echo $REGISTRY
	echo $NAME
	echo $TAG
	docker pull "$REGISTRY/$NAME:$TAG"
    (( INDEX++ ))
done


#  ImageRegistryCheck.py
echo ">>> Scanning Image Registry ...."
chmod +x ~/xAppSec/Image_Security_Module/ImageRegistryCheck.py
../Image_Security_Module/ImageRegistryCheck.py registry-check $NAME

#  Backdoor_Scan.py
echo ">>> Scanning If Backdors Within Image...."
chmod +x ~/xAppSec/Image_Security_Module/backdoor_scan.py
../Image_Security_Module/backdoor_scan.py xapp-scan-images $NAME

#  ImageHistory_Scan.py
echo ">>> Scanning History Instructions in the Image...."
cd ~/xAppSec/Image_Security_Module/
chmod +x image_history.py
../Image_Security_Module/image_history.py xapp-scan-images $NAME
#  Ask if want to install the xApp

kubectl get pods 

echo "+------------------------------+"

until [ "${ANSWER}" == "Y" ] || [ "${ANSWER}" == "N" ] 
do 
   read -p "If you want to install the xApp.(Y/N) ? " ANSWER
done 

if [ "${ANSWER}" != "Y" ]
then
  echo "Bye Bye."
  exit
fi 
#  Install the xApp (If yes)

XAPP_NAME=$(cat  ${CONFIG_JSON}  | jq -c ".xapp_name"| tr -d '"')
XAPP_VERSION=$(cat  ${CONFIG_JSON}  | jq -c ".version"| tr -d '"')
echo "Installing xApp ...."
dms_cli install $XAPP_NAME $XAPP_VERSION ricxapp

sleep 10
#  Check if xApp is in "Running" State
kubectl get pods -n ricxapp

#  Return the Kibana Service Address
URL=$(kubectl get svc | grep kibana-np | cut -c 29-43| tr -d " ")
echo "Now You Can Acces the Kibana Service."
echo "Kibana URL: http://${URL}:8080/" 
