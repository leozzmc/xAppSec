# xAppSec 
<div align="left">
<img src=https://user-images.githubusercontent.com/30616512/163117059-1aec6465-81c5-4946-97be-d76b365a79d2.png  width="20%" height="20%"  />
</div>

A command tool to perform the security check to xApp and set up EFK stack for monitoring xApp's behavior.

## Environment.
```
✅ Working well in Near-RT RIC Cluster [E Release]
✅ Ubuntu 18.04 LTS
```

## Funcitonality

```
xAppSec Usage:

./xAppSec.sh [OPTIONS]

[OPTIONS]:image
 -i: initialize the envrionment.
 -n: normal mode, do xApp image scanning,onboarding and installing the xApp.
 -k: Setup Kibana Index Pattern.
 -h: Help.
```

- Setup Environment for xApp image scanning, onboarding and deploying.
- Deploy EFK Stack for monitoring xApp's behavior.
- Automatically Setup Kibana Index Pattern.

## Initialization
The initialization includes  the following steps:
- Install VeinMind SDK and related dependencies.
- Clone O-RAN xapp_onboarder repo.
- Build custom fluentd daemonset dockerfile.
- Deploy EFK K8S objects.
- Run helm server locally.
## Image Scan
Run the following script for scanning xApp's image.
- `ImageRegistryCheck.py`
- `backdoor_scan.py`
- `image_history.py`

## EFK Monitoring
Capture xApp's Pod log and present its behavior.
- Create Index Pattern automatically. 

## Process
#### 程式運作-xApp進駐與鏡像檢查
![程式運作-xApp進駐與鏡像檢查](https://user-images.githubusercontent.com/30616512/171382056-fb84ebcf-95d1-4944-9012-9eb451cbabc1.png)

#### 程式運作-EFK
![程式運作-EFK](https://user-images.githubusercontent.com/30616512/171382080-82960ccc-e245-42fd-a031-c695483cc366.png)

