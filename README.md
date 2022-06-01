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

## Architecture

<img width="460" alt="image" src="https://user-images.githubusercontent.com/30616512/171382623-91449fd2-f32a-4076-88c6-e7ef3e2ee0f2.png">


## Process
#### 程式運作-xApp進駐與鏡像檢查
<img width="460" alt="image" src="https://user-images.githubusercontent.com/30616512/171382684-833069df-4765-4cf7-8bcc-9146d8b0b731.png">

#### 程式運作-EFK進行日誌處理
<img width="460" alt="image" src="https://user-images.githubusercontent.com/30616512/171382741-35946276-5c15-4381-8a90-89796e7e87d6.png">

## Execution

```
./xAppSec.sh -i
```
<img width="460" alt="image" src="https://user-images.githubusercontent.com/30616512/171382418-35697590-0e40-44a5-9c0d-d153daf701eb.png">



