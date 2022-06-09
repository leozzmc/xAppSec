#!/bin/bash
cd ~
ROOTDIR=$(pwd)
cd ~/xAppSec/Testing/test_case/xApp_descriptor/ad 
echo ">>> Building fake ad xApp..."
docker build -t nexus3.o-ran-sc.org:10002/fake_ad_xapp:0.0.1 .
cd ..
echo ">>> fake AD xApp descriptor config file path: "
echo "$(pwd)/malicious_ad_config.json"

cd ~/xAppSec/Testing/test_case/xApp_descriptor/qp 

## Running Private Registry
echo "Running Private Registry..."
docker run -d -p 5000:5000 --name private_registry --restart always registry:latest


echo ">>> Building fake qp xApp..."
docker build -t 127.0.0.1:5000/fake_qp_xapp:0.0.1 .
docker push 127.0.0.1:5000/fake_qp_xapp:0.0.1
cd ..
echo ">>> fake QP xApp descriptor config file path: "
echo "$(pwd)/malicious_qp_config.json"