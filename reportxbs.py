from requests import Session
import pandas as pd
import random

session = Session()
print("制作: 2302 No.10")
a = int(input("请先搜索新百胜,然后输入帖子页数:"))
hasReported = 0
xlsx = pd.read_excel("./acc.xlsx")

maxNum = 290

for i in range(a):

    res_searchForums = session.get(
        "https://api.codemao.cn/web/forums/posts/search?title=新百胜&limit=20&page="+str(i+1))
    forums = res_searchForums.json()
    items = forums["items"]
    for j in items:
        title = j["title"]
        xbs = 0
        xbsWord = ["com", "vip", "网址", "游戏", "登录", "注册", "靠谱", "集团",
                   "火爆", "投资", "联系", "咨询", "解决", "直属", "怎么", "真人", "网投"]
        for k in xbsWord:
            if (k in title):
                xbs += 1
        isXbs = False
        if (xbs >= 2):
            isXbs = True
        if (isXbs):
            id = str(j["id"])
            reportData = {
                "post_id": id,
                "description": "新百胜",
                "reason_id": "1"
            }
            iden = random.randint(10,maxNum)
            acc = xlsx.iat[iden, 0]
            pas = xlsx.iat[iden, 1]
            # print(acc,pas)
            login_data = {'pid': '65edCTyg',
                          'identity': str(acc),
                          'password': str(pas)}
            res_login = session.post(
                'https://api.codemao.cn/tiger/v3/web/accounts/login', json=login_data)
            # print(str(res_login.content, "utf-8"))
            res_report = session.post(
                "https://api.codemao.cn/web/reports/posts", json=reportData)
            print(str(res_report.content, "utf-8"))
            hasReported += 1

print("程序执行完毕,本次举报了", hasReported, "个新百胜")
input()
