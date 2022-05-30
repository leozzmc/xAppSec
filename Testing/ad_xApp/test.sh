#!/bin/bash

CONTAINER_NUM=$(cat config.json | jq -c ".containers" | jq length)
declare -a IMAGE_SET=()


INDEX=0
while [ $INDEX -lt  $CONTAINER_NUM ]
do
    REGISTRY+=$(cat config.json | jq -c ".containers[$INDEX].image.registry"| tr -d '"')
    REGISTRY+=$(cat config.json | jq -c ".containers[$INDEX].image.name"| tr -d '"')
    REGISTRY+=$(cat config.json | jq -c ".containers[$INDEX].image.tag" | tr -d '"')
    #REGISTRY+=$($REGISTRY | tr -d '"')
    echo "$REGISTRY"
    IMAGE_SET+=($REGISTRY)
    echo $IMAGE_SET
    (( INDEX++ ))
done

docker pull $IMAGE_SET
