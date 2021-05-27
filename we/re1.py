import json

import requests

# data = {
#     "grant_type": "client_credentials",
#     "client_id": "MaUKHygRgxEXIrGi52csa6bbcCvydyGn",
#     "client_secret": "y7f8GzI9naakKEltjMvsPrm8sxtiutfw",
#     "scope": "basic,netdisk"
# }
# with open("./txt.txt") as f:
#     lines = []
#     for i in f.readlines():
#         lines.append(i[:-1])
#     if len(lines) == 2:
#         access_token = lines[0]
#         refresh_token = lines[1]
# with open("./txt.txt", "w") as f:
#     if len(lines) != 2:
#         r = requests.post('https://openapi.baidu.com/oauth/2.0/token', data=data)
#         print(json.loads(r.content))
#         access_token = json.loads(r.content)["access_token"]
#         refresh_token = json.loads(r.content)["refresh_token"]
#         f.write(access_token + "\n")
#         f.write(refresh_token + "\n")
#
# print(access_token, refresh_token)
#
# params = {"access_token": access_token}
# r = requests.get("https://pan.baidu.com/api/quota", params=params)
# print(r.url)

params = {
    "response_type": "token",
    "client_id": "MaUKHygRgxEXIrGi52csa6bbcCvydyGn",
    "redirect_uri": "oob",
    "scope": "basic,netdisk",
    "display": "popup",
    # "state": "xxx"
}
r = requests.get("https://openapi.baidu.com/oauth/2.0/authorize", params=params)
print(r.url)
print(r.content)
