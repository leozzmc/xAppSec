#!/bin/bash


#### 0. Store the parameters from user

read -p "😎 Please provide the path to your xApp descriptor configuration file: " CONFIG_JSON
read -p "😎 Please provide the path to your xApp descriptor schema file: " SCHEMA_JSON
echo  -e "\n📂 xApp Descriptor Config.json Path:" ${CONFIG_JSON} 
echo  -e "📂 xApp Descriptor Schema.json Path:" ${SCHEMA_JSON}

#### 1. Install dms_cli tool
echo "🕓   Installaling the dms_cli tool -------------------------"
sleep 2

sudo apt-get install -y python3-pip jq
git clone "https://gerrit.o-ran-sc.org/r/ric-plt/appmgr"
cd appmgr/xapp_orchestrater/dev/xapp_onboarder
pip3 install ./
sudo chmod 755 /usr/local/bin/dms_cli

#### 2. Run the local helm server
echo "🕓   Running the local helm server -------------------------"
sleep 2

docker run --rm -u 0 -it -d -p 8080:8080 \
    -e DEBUG=1 \
    -e STORAGE=local \
    -e STORAGE_LOCAL_ROOTDIR=/charts \
    -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest 

export CHART_REPO_URL=http://0.0.0.0:8080

#### 3. Received the xApp Config.json and Scehma.json to onboard xApp
echo "🕓   Starting to onboard the xApp --------------------------"
sleep 2

dms_cli onboard  ${CONFIG_JSON} ${SCHEMA_JSON}

curl -X GET http://localhost:8080/api/charts | jq .


#### 4. Call the Static Analysis Function
echo "🧫   Perform static analysis to the xApp -------------------"
sleep 2

######  4.1 Helm Charts Analysis

#  Note
#  dms_cli install_values_yaml hwxapp 1.0.0 ricxapp --output_path=.
#  Q1: How to get the xApp name and version number?
#  A1: Use " cat config-file.json | jq -c '.version' " and " cat config-file.json | jq -c '.xapp_name' "

XAPP_NAME=$(cat ${CONFIG_JSON} | jq -c '.xapp_name')
XAPP_VERSION=$(cat ${CONFIG_JSON} | jq -c '.version')

dms_cli install_values_yaml ${XAPP_NAME} ${XAPP_VERSION} ricxapp  --output_path=.


######  4.2 Image Regsitry Check

CONTAINER_NUM=$(cat $CONFIG_JSON | jq -c ".containers" | jq length)
declare -a REGISTRY=()

# Store the container registrys to array
INDEX=0
while [ $INDEX -lt  $CONTAINER_NUM ]
do
	REGISTRY+=($(cat $CONFIG_JSON | jq -c ".containers[$INDEX].image.registry"))
	echo "[$INDEX] | Value: ${REGISTRY[$INDEX]}"
	(( INDEX++ ))
done


# Compare with whitelist
declare -a White







######  4.3 Image Vulnerabities Check


#### 5. dms_cli tool install the xApp



#### 6. Continuously check the deployment of xApp

#### 7. Call the Dynamic Security Analysis function
