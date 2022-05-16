# Requirements for Initialization
## For Image_Scan

- 所需依賴套件

```bash
sudo apt install -y python3-pip
```

- 運行VeinMnd SDK

```bash
# 添加 VeinMind SDK 的 APT Repository
echo 'deb [trusted=yes] https://download.veinmind.tech/libveinmind/apt/ ./' | sudo tee /etc/apt/sources.list.d/libveinmind.list

# 安裝 VeinMind SDK
sudo apt-get update
sudo apt-get install libveinmind-dev
```

- 為運行三隻掃描程式

```bash
cd ~/xAppSec/Image_Security_Module/
pip3 install -r requirements.txt
```

requirements.txt之中包含
- `click==7.1.2`
- `jsonpickle==2.1.0`
- `veinmind==1.0.6`
- `pytoml==0.1.21`

## For Running EFK Stack

- Elasticsearch → 7.5.0
- Kibana → 7.5.0
- Fluentd(Image) → 1.14.6