#!/bin/bash

# Create Kibana Index Pattern 
KIBANA_EP=$(kubectl get ep| grep kibana-np|cut -c 15-35| tr -d " ")

echo "Sending API Request to Kibana service ...."

curl -X GET $KIBANA_EP/api/saved_objects/_find?type=index-pattern&search_fields=title&search=xapp-* -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '
{
  "attributes": {
    "title": "my-search",
    "timeFieldName": "@timestamp"
  }
}'


# Add Scripted Field in Kibana
if (doc['kubernetes.namespace_name.keyword'].size() != 0 ){
  if (doc['message.keyword'].size() != 0){
    if (doc['msg.keyword'].size() != 0 ){
      if (doc['message.keyword'].size() == doc['msg.keyword'].size()){
        return doc['message.keyword'].value;
      }
    }
    else if (doc['log.keyword'].size() != 0 ){
      if (doc['message.keyword'].size() == doc['log.keyword'].size()){
        return doc['message.keyword'].value;
      }
    }
  }
  else if (doc['log.keyword'].size() != 0){
    if (doc['msg.keyword'].size() != 0 ){
      if (doc['log.keyword'].size() == doc['msg.keyword'].size()){
        return doc['log.keyword'].value;
      }
    }
  }
}