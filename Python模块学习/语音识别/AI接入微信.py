# -*- coding: utf-8 -*-
# @Author : ZX
# @File : AI接入微信
# @Software: PyCharm
# @Date : 2024/7/28


import requests
import json
from wxauto import WeChat


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=BAC91d32ppYad38FFd4Uv0tK&client_secret=G4gUSviPqBAgXi3Yx2bcnppPRaL1s8kM"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def main(wx, msg):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": msg
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_result = json.loads(response.text)
    print(json_result)
    # print(response.text)
    wx.SendMsg(msg=json_result['result'] + "--此内容为AI生成", who="干部摸鱼群(无老师版)")


if __name__ == '__main__':
    wx = WeChat()
    while True:
        msgs = wx.GetAllMessage()
        if msgs:
            if msgs[-1].type == "friend":
                main(wx, msgs[-1].content)
