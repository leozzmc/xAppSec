#!/bin/bash

# Create Kibana Index Pattern 
KIBANA_EP=$(kubectl get ep| grep kibana-np|cut -c 15-35| tr -d " ")

echo "Sending API Request to Kibana service ...."
echo "Testing Script."

# Add Scripted Field in Kibana
curl -X POST $KIBANA_EP/api/saved_objects/index_pattern/index-pattern-id/runtime_field -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '
{
  "name": "xapp-*",
  "TestField": {
     "type": "string",
     "script": {
        "lang": "painless",
        "source": """
          if (doc['kubernetes.namespace_name.keyword'].size() != 0 && doc['stream.keyword'].value == "stderr" ){
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
        """
      }
  }
}'


# if (doc['kubernetes.namespace_name.keyword'].size() != 0 && doc['stream.keyword'].value == "stderr" ){
#   if (doc['message.keyword'].size() != 0){
#     if (doc['msg.keyword'].size() != 0 ){
#       if (doc['message.keyword'].size() == doc['msg.keyword'].size()){
#         return doc['message.keyword'].value;
#       }
#     }
#     else if (doc['log.keyword'].size() != 0 ){
#       if (doc['message.keyword'].size() == doc['log.keyword'].size()){
#         return doc['message.keyword'].value;
#       }
#     }
#   }
#   else if (doc['log.keyword'].size() != 0){
#     if (doc['msg.keyword'].size() != 0 ){
#       if (doc['log.keyword'].size() == doc['msg.keyword'].size()){
#         return doc['log.keyword'].value;
#       }
#     }
#   }
# }