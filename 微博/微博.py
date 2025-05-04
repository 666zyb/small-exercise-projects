import requests
from lxml import etree


def crawl(keyword,page):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://s.weibo.com/weibo?q=%E7%88%AC%E8%99%AB&page=2",
        "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit"
    }
    cookies = {
        # "SINAGLOBAL": "6814354702343.719.1732580398678",
        # "SCF": "AiSiW69ujdWkUISteEvK14ifOV-aCMgy2MBpi-_bo_ZfAZ3aeCAdv_SB93PRAvACf_f6mNCSG676vWxjOSiL3f8.",
        "SUB": "_2A25KsumeDeRhGeFH41AW9ibPzD6IHXVpzmNWrDV8PUNbmtANLWbikW9Nel39gaIu3cWIdb6dTNRsxiqgz3m2KaFy",
        # "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFWpDihRRmi73-Z7A-AwD4Z5NHD95QN1KnES0qRe0MEWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.ReoMc1heNentt",
        # "ALF": "02_1742612174",
        # "_s_tentry": "passport.weibo.com",
        # "Apache": "4622891979405.506.1740020179662",
        # "ULV": "1740020179706:2:1:1:4622891979405.506.1740020179662:1732580398699"
    }
    url = "https://s.weibo.com/weibo"
    params = {
        # "q": "你好",
        # "page": "4",
    }
    params['q'] = str(keyword)
    params['page']=str(page)
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    tree=etree.HTML(response.content)
    content=tree.xpath('//div[@class="card-wrap"]/div[@class="card"]//p[@class="txt"]')
    for i in content:
        print(str(i.text).strip())

keyword=input("输入关键词:")
for page in range(1,11):
    crawl(keyword,page)