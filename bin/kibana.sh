#!/bin/bash

# Create Kibana Index Pattern 
KIBANA_EP=$(kubectl get ep| grep kibana-np|cut -c 15-35| tr -d " ")

echo "Sending API Request to Kibana service ...."

curl -X POST $KIBANA_EP/api/saved_objects/index-pattern/index-pattern-id  -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '
{
  "attributes": {
    "title": "xapp-*",
    "timeFieldName": "@timestamp"
  }
}'


