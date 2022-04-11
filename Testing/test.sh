#!/bin/bash

# store registrys to array
TEST_CONFIG_JSON=$(pwd)/test.json
echo $TEST_CONFIG_JSON

CONTAINER_NUM=$(cat $TEST_CONFIG_JSON | jq -c ".containers" | jq length)
echo "Container Numbers: $CONTAINER_NUM"
declare -a REGISTRY=()

INDEX=0
while [ $INDEX -lt  $CONTAINER_NUM ]
do
	REGISTRY+=($(cat $TEST_CONFIG_JSON | jq -c ".containers[$INDEX].image.registry"))
	echo "[$INDEX] | Value: ${REGISTRY[$INDEX]}"
	(( INDEX++ ))
done
echo "📑 Comparing with whitelist ..."

#python3 /mnt/c/Users/Kevin/xAppSecProject/xAppSec/script/ImageRegistryCheck.py $TEST_CONFIG_JSON
/mnt/c/Users/Kevin/xAppSecProject/xAppSec/script/ImageRegistryCheck_modified.py ##registry_check $TEST_CONFIG_JSON



