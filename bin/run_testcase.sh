#!/bin/bash
cd ~
ROOTDIR=$(pwd)
cd ~/xAppSec/Testing/test_case/xApp_descriptor/ad 
echo ">>> Building fake ad xApp..."
docker build -t nexus3.o-ran-sc.org:10002/fake_ad_xapp:0.0.1 .
cd ..
echo ">>> fake xApp descriptor config file path: "
echo "$(pwd)/malicious_ad_config.json"