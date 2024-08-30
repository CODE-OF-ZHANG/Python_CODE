import requests
import argparse
from datetime import datetime, timedelta


class CsdnCommentsCounter:
    @staticmethod
    def get_comments_count(username, date):
        # 构建API URL
        api_url = f"https://blog.csdn.net/community/home-api/v1/comment-list?page=1&size=220&type=out&noMore=false" \
                f"&username={username} "

        headers = {
            "host": "blog.csdn.net",
            "connection": "keep-alive",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "user-agent": "hello",
            "cookie": "world",
            "accept": "application/json, text/plain, */*",
            "origin": "https://mp.csdn.net",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://mp.csdn.net/mp_blog/manage/article?spm=1011.2419.3001.5298",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8"
        }

        # 发起GET请求
        response = requests.get(api_url, headers=headers)

        # dump
        # print(response.text)

        # 检查响应是否成功
        if response.status_code != 200:
            print(f"请求出错: {response.status_code}")
            return -1

        # 尝试解析JSON
        try:
            data = response.json()
            comments = data['data']['list']
            target_date_comments = [comment for comment in comments if comment['createTime'].split()[0] == date]
            return len(target_date_comments)
        except ValueError as e:
            print(f"JSON解析出错: {e}")
            return -1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSDN Comments Manager')

    # 命令行参数，用于指定用户名
    parser.add_argument('-u', '--username', type=str, default='dh45498', help='username to get today comments count')
    args = parser.parse_args()
    # dh45498  爱喝兽奶的荒天帝

    # 获取今天的评论数量
    today_date = datetime.now().strftime('%Y-%m-%d')
    today_count = CsdnCommentsCounter.get_comments_count(args.username, today_date)
    print(f"爱喝兽奶的荒天帝 今天的评论数量为: {today_count}")

    # 获取昨天的评论数量
    yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    yesterday_count = CsdnCommentsCounter.get_comments_count(args.username, yesterday_date)
    print(f"爱喝兽奶的荒天帝 昨天的评论数量为: {yesterday_count}")

    print(f"爱喝兽奶的荒天帝 最近2天的评论总数量为: {yesterday_count + today_count}")
