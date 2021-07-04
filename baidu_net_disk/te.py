import requests
import json


class MyNetDisk:
    headers = {
        'User-Agent': 'pan.baidu.com'
    }

    def __init__(self, token, refresh_token):
        self.token = token
        self.refresh_token = refresh_token

    def get_file_list(self, path):
        url = "https://pan.baidu.com/rest/2.0/xpan/file"
        payload = {
            'access_token': self.token,
            'method': 'list',
            'dir': path
        }
        response = requests.request("GET", url, headers=MyNetDisk.headers, params=payload)
        print(response.url)
        x = json.loads(response.text)
        return x

    def get_video_list(self):
        url = "https://pan.baidu.com/rest/2.0/xpan/file"
        payload = {
            'access_token': self.token,
            'method': 'videolist',
        }
        response = requests.request("GET", url, headers=MyNetDisk.headers, params=payload)
        print(response.url)
        x = json.loads(response.text)
        return x



a = MyNetDisk(
    "121.dd392bab8674d2de51f28b3c15551d16.Y_2tNzfwLR-TWRMhq0B6DYZwQp1l9yGJu_wMvOn.kcjyvA",
    "122.074a9bd93d71fac11c27823371fece4e.YHKwk-7oOVaGvoTO20X7xUVUkJXAYGQWx8MDJiL.BvpTyQ"
)

print(a.get_video_list())
