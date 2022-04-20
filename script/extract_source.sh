#!/bin/bash


## For testing
TEST_CONFIG_JSON=$(pwd)/../Testing/test.json
CONTAINER_NUM=$(cat $TEST_CONFIG_JSON | jq -c ".containers" | jq length)
echo "Container Numbers: $CONTAINER_NUM"

## Step 0 - Get the container name

## CONTAINER_ID=kubectl get pod <ricxapp_name> -n ricxapp  -o jsonpath='{.status.containerStatuses[0].containerID}'
## CONTAINER_NAME=${CONTAINER_ID##docker://}
## echo $CONTAINER_NAME
## ( [0] means it is the first container in the pod )


## Step 1 -  docker inspcet <container_name>  


### 1.1   Get  "WorkingDir"
## docker inspect --format={{.Config.WorkingDir}} $CONTAINER_NAME
### 1.2   Get "CMD" 
## docker inspect --format={{.Config.Cmd}} $CONTAINER_NAME     ## It can retrive the command to be executed in container.
### 1.3.  Judge the source code is .c, .py, .go or bash file

## Step 2 -  docker cp <container_name>:</path/to/the/file> </local/system/path>

## Step 3  - Return source code path

# Test

# conflict test
# conflict test
