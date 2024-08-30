# 导入requests模块
import requests

# 获取360翻译的翻译的数据包地址
url = 'https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=hello'
# 获取请求头等伪装信息
head = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Length': '0',
    'Cookie': 'QiHooGUID=F02A63E0BCB72DB4A01C21FA023475E1.1703769301607; Q_UDID=00b0237e-501b-1360-b2eb-96b79d1ac5ec; __guid=144965027.253643186935022000.1703769305042.223; count=2',
    'Origin': 'https://fanyi.so.com',
    'Pro': 'fanyi',
    'Referer': 'https://fanyi.so.com/',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 运行之后可以反复翻译
while 1:
    # 改变query的值
    word = input('请输入你要翻译的内容:')
    # 获取输入的内容是中文还是英文
    lenght = len(word[0].encode('utf-8'))
    # 判断,如果输入的是中文,这翻译为英文;如果输入的是英文,这翻译为中文
    if lenght == 3:
        eng = 0
    else:
        eng = 1
    # post请求所需要的额外参数(数据类型为字典数据类型)
    data_dic = {
        'eng': eng,
        'ignore_trans': 0,
        'query': word
    }
    # 发送请求，获取响应
    res = requests.post(url, headers=head, data=data_dic)
    # 将响应内容转化成json数据类型
    data = res.json()
    # 打印翻译内容
    print(data['data']['fanyi'])
