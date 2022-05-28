#!/bin/bash
#'''This script is for initializing the xAppSec environment.'''

#  Install VeinMind SDK
echo ">>> Downloading VeinMind SDK...."
echo 'deb [trusted=yes] https://download.veinmind.tech/libveinmind/apt/ ./' | sudo tee /etc/apt/sources.list.d/libveinmind.list
sudo apt-get update
sudo apt-get install -y libveinmind-dev
#  Install Dependencies
echo ">>> Downloading Dependencies...."
sudo apt-get install -y python3-pip jq
pip3 install -r  ../Image_Security_Module/requirements.txt
sudo apt-get install nfs-common
#  Build fluentd image
echo ">>> Building Fluentd Docker Image...."
cd ~/xAppSec/Config/Fluentd-DS_Config
docker build -t myfluentd:latest . --no-cache
#  Install NFS Server (if needed)
#  Create Storage Classes
echo ">>> Creating Storage Classes...."
cd ~/xAppSec/EFK_Deployer
kubectl create -f class.yaml
#  Create Elasticsearch Service and StatefulSet
echo ">>> Creating Elasticsearch Service and StatefulSet...."
cd ~/xAppSec/EFK_Deployer/elasticsearch
kubectl create -f es-svc.yaml
kubectl create -f es-sts.yaml
#  Create Kibana Service and Deployment
echo ">>> Creating Kibana Service and Deployment...."
cd ~/xAppSec/EFK_Deployer/kibana
kubectl create -f kibana-svc.yaml
kubectl create -f kibana-deployment.yaml
#  Create Fluentd Service Account、Fluentd ClusterRole、Fluentd ClusterRoleBinding、Fluentd DaemonSet
echo ">>> Creating Fluentd...."
cd ~/xAppSec/EFK_Deployer/fluentd_test
kubectl create -f fluentd-sa.yaml
kubectl create -f fluentd-role.yaml
kubectl create -f fluentd-rb.yaml
kubectl create -f fluentd-ds.yaml
#  Run Local Helm Server
echo ">>> Running Local Helm Server"
export CHART_REPO_URL=http://0.0.0.0:8080
docker run --rm -u 0 -it -p 8080:8080 -e DEBUG=1 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/charts -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest 




