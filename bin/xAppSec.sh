#!/bin/bash

#### 0. Store the parameters from user

read -p "😎 Please provide the path to your xApp descriptor configuration file: " CONFIG_JSON
read -p "😎 Please provide the path to your xApp descriptor schema file: " SCHEMA_JSON
echo  -e "\n📂 xApp Descriptor Config.json Path:" ${CONFIG_JSON} 
echo  -e "📂 xApp Descriptor Schema.json Path:" ${SCHEMA_JSON}

#### 1. Install dms_cli tool

#### 2. Run the local helm server

#### 3. Received the xApp Config.json and Scehma.json to onboard xApp

#### 4. Call the Static Analysis Function

#### 5. dms_cli tool install the xApp

#### 6. Continuously check the deployment of xApp

#### 7. Call the Dynamic Security Analysis function
