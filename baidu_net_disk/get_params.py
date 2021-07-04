import json

import requests

AppID = '23911194'
AppKey = '76UqaqSahccmAGWvXRviqKCLnlGwCV3M'
SecretKey = 'gV1fbTtnTvmGup6n4nLi1iLUy6DGC6GY'
SignKey = '3NNnvIs4vkdA*6NS=D-uZ-Ot*++aWheB'

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
    "response_type": "code",
    "client_id": AppKey,
    "redirect_uri": "oob",
    "scope": "basic,netdisk",
    # "scope": "email",
    "display": "popup",
    # "state": "xxx"
}
r = requests.get("https://openapi.baidu.com/oauth/2.0/authorize", params=params)
print(r.url)
print(r.text)

AuthorizationCode = '4572a161229005788311594c5a53ca9c'

#  通过上面第一步获得Authorization Code后，便可以用其换取一个Access Token。获取方式是，应用在其服务端程序中发送请求（推荐使用POST）到 百度OAuth2.0授权服务的“https://openapi.baidu.com/oauth/2.0/token”地址上，并带上以下5个必须参数：
#
# grant_type：必须参数，此值固定为“authorization_code”；
# code：必须参数，通过上面第一步所获得的Authorization Code；
# client_id：必须参数，应用的API Key；
# client_secret：必须参数，'应用的Secret Key；
# redirect_uri：必须参数，该值必须与获取Authorization Code时传递的“redirect_uri”保持一致。

params = {
    "grant_type": "authorization_code",
    "code": AuthorizationCode,
    "client_id": AppKey,
    "client_secret": SecretKey,
    "redirect_uri": "oob",
}
r = requests.get("https://openapi.baidu.com/oauth/2.0/token", params=params)
print(r.url)
print(r.text)

access_token = '121.dd392bab8674d2de51f28b3c15551d16.Y_2tNzfwLR-TWRMhq0B6DYZwQp1l9yGJu_wMvOn.kcjyvA'
refresh_token = '122.074a9bd93d71fac11c27823371fece4e.YHKwk-7oOVaGvoTO20X7xUVUkJXAYGQWx8MDJiL.BvpTyQ'

# url = "https://pan.baidu.com/rest/2.0/xpan/nas"
#
# payload = {
#     'access_token': access_token,
#     'method': 'uinfo'
# }
# headers = {
#     'User-Agent': 'pan.baidu.com'
# }
#
# response = requests.request("GET", url, headers=headers, params=payload)
# print(response.url)
#
# print(response.text)


