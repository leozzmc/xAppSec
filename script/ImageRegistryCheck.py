import json
import sys

config_file = sys.argv[1]
#schema_file = sys.argv[2]

### Local Testing###
# config_file = "/mnt/c/Users/Kevin/xAppSecProject/xAppSec/Testing/hw_xApp/config-file.json"
# schema_file = "/mnt/c/Users/Kevin/xAppSecProject/xAppSec/Testing/hw_xApp/schema.json"
#test_json = "/mnt/c/Users/Kevin/xAppSecProject/xAppSec/Testing/test.json"

Registry_List = []
While_List = ["nexus3.o-ran-sc.org:10002"]

with open(config_file,"r") as configfile:
    data = json.load(configfile)

for i in range(0, len(data['containers']) ):
    Registry_List.append(data['containers'][i]['image']['registry'])
    print(Registry_List[i])

configfile.close()

for i in Registry_List:
    if i != "nexus3.o-ran-sc.org:10002":
        print (f"\n❎ the image registry: \"{i}\" of xApp is invalid!")



#####  Should Write to Analysis Result File ! ##########
#                                                      #
#                                                      #
#                                                      #
########################################################