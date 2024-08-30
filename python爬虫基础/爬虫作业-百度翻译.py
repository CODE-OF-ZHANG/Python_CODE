# 导入requests模块
import requests

# 请求百度翻译网址
url = 'https://fanyi.baidu.com/sug'
# 伪装
head = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '8',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=62BC9BD37C69A8C1335433839C4FB9BD; PSTM=1694964869; BAIDUID=62BC9BD37C69A8C121D5BAF364E4B08E:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=39713_39817_39841_39903_39909_39934_39937_39933_39941_39938_39931_39997_39661; H_WISE_SIDS_BFESS=39713_39817_39841_39903_39909_39934_39937_39933_39941_39938_39931_39997_39661; BAIDUID_BFESS=62BC9BD37C69A8C121D5BAF364E4B08E:FG=1; ZFY=:AvSaJDjE31c7auqWOSN78273yKU7FlDqCp2WwuhSJ7g:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39938_39997_40011_40041; BDUSS=dlZFlmQjdqbWFhMWhZOVJaZ1NiMWQ1b3A4Y2FuSllFUXlpNG1JUTk2S0ctYlJsSVFBQUFBJCQAAAAAAQAAAAEAAAClYxo8n2~Venp4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZsjWWGbI1lUH; BDUSS_BFESS=dlZFlmQjdqbWFhMWhZOVJaZ1NiMWQ1b3A4Y2FuSllFUXlpNG1JUTk2S0ctYlJsSVFBQUFBJCQAAAAAAQAAAAEAAAClYxo8n2~Venp4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZsjWWGbI1lUH; RT="z=1&dm=baidu.com&si=5ffc2244-09c5-4d65-8840-83b81b106878&ss=lqp6zjiz&sl=9&tt=2fv&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=q5s&nu=9y8m6cy&cl=oqj&ul=to1&hd=to7"; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1703769234; BA_HECTOR=258h2g0121a42lak0580a10l6c4ib81ioqt6o1s; delPer=0; PSINO=6; BCLID=7587126060499642979; BCLID_BFESS=7587126060499642979; BDSFRCVID=Y5POJexroG3O1HvqZR0qrpCqW_weG7bTDYrEOwXPsp3LGJLVFdWiEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=Y5POJexroG3O1HvqZR0qrpCqW_weG7bTDYrEOwXPsp3LGJLVFdWiEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsX6QTB2Q-XPoO3KOchqnCKq6CDb_XK-bDLhRf5mkf3fbgy4op8P3y0bb2DUA1y4vp0t3U2mTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_2jjQL3J; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsX6QTB2Q-XPoO3KOchqnCKq6CDb_XK-bDLhRf5mkf3fbgy4op8P3y0bb2DUA1y4vp0t3U2mTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_2jjQL3J; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1702096989,1703768101,1703827735; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1703827746; ab_sr=1.0.1_Nzg1N2VjNGEyMmMwMjA1N2RkYWU4ZTg2M2IwNmEyNzdhNWQ4NzBmMDQyMmFiNWEwMDJiOTllYzM5OGNkOWJmYTM0NjNkYmIxNWVkMmNmNGQ0ZTE0YTlmZmU0YTUzYTA3NjQ5OTUwMWVhY2RiZGRiOGZhMzRkMDI2MGY3OTEzZjE5NzJiZTBlYjY4OTA0YjM5YzU5MTk4ZDYwNTczZWU5OTg0NTljMjU4Zjk3YmZhOWQ1MGI2YmVmY2RkZDhkN2U1',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
# 循环输入，运行一次可翻译多次，知道终止程序
while 1:
    word = input('请输入要翻译的单词:')
    # post请求 请求需要携带的额外参数(字典数据类型)
    data_dic = {
        'kw': word
    }
    # 发送请求,获取响应
    res = requests.post(url, headers=head, data=data_dic)
    # 将响应内容转化为json格式
    data = res.json()
    # 打印
    print(data['data'][0]['v'])
# 这个只能翻译单词，不能翻译句子
