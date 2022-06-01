# xAppSec 
<div align="left">
<img src=https://user-images.githubusercontent.com/30616512/163117059-1aec6465-81c5-4946-97be-d76b365a79d2.png  width="20%" height="20%"  />
</div>

Building the command tool to perform the security analysis to xApp in both static and dynamic ways.

## Funcitonality

```
xAppSec Usage:

./xAppSec.sh [OPTIONS]

[OPTIONS]:
 -i: initialize the envrionment.
 -n: normal mode, do xApp image scanning,onboarding and installing the xApp.
 -k: Setup Kibana Index Pattern.
 -h: Help.
```

- Setup Environment for xApp image scanning, onboarding and deploying.
- Deploy EFK Stack for monitoring xApp's behavior.
- Automatically Setup Kibana Index Pattern.