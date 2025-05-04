import requests
import json


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json; charset=UTF-8",
    "origin": "https://wallspic.com",
    "priority": "u=1, i",
    "referer": "https://wallspic.com/cn/tag/jian_yue/3840x2160",
    "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "PHPSESSID": "affa24e8dac8bbd4ebe7ada11ae82abcc73ef3a42d572773c6da7513ad6a9ab2",
    "_ga_DCNLH4PLY3": "GS1.1.1738999942.1.0.1738999942.0.0.0",
    "_ga": "GA1.1.86800369.1738999942",
    "__gads": "ID=66a5ee3bf1cb909a:T=1738999943:RT=1738999943:S=ALNI_MYDO57B1YgLgbrYrUTIBRIz1DIXHg",
    "__gpi": "UID=0000102d4ad8b00a:T=1738999943:RT=1738999943:S=ALNI_MYBFhTv-fXJYwmBA5DSTMg3LuQNEQ",
    "__eoi": "ID=98d1c5bb423362db:T=1738999943:RT=1738999943:S=AA-AfjYp_aAYYByBRHlSjem44DRw",
    "theme": "theme-dark"
}
url = "https://wallspic.com/api/gallery"
params = {
    "locale": "cn"
}
data = {
    "galleryTarget": {
        "tag": {
            "id": 151,
            "is_active": 1,
            "main_pic_id": 2237,
            "pics_total": 251,
            "translation": {
                "ar": {
                    "id": 151,
                    "langtag": "ar",
                    "title": "تقليلية",
                    "slug": "tqlylyt"
                },
                "cn": {
                    "id": 151,
                    "langtag": "cn",
                    "title": "简约",
                    "slug": "jian_yue"
                },
                "de": {
                    "id": 151,
                    "langtag": "de",
                    "title": "Minimalismus",
                    "slug": "minimalismus"
                },
                "en": {
                    "id": 151,
                    "langtag": "en",
                    "title": "minimalism",
                    "slug": "minimalism"
                },
                "es": {
                    "id": 151,
                    "langtag": "es",
                    "title": "el minimalismo",
                    "slug": "el_minimalismo"
                },
                "fr": {
                    "id": 151,
                    "langtag": "fr",
                    "title": "minimalisme",
                    "slug": "minimalisme"
                },
                "ja": {
                    "id": 151,
                    "langtag": "ja",
                    "title": "ミニマリズム",
                    "slug": "minimarizumu"
                },
                "pt": {
                    "id": 151,
                    "langtag": "pt",
                    "title": "minimalismo",
                    "slug": "minimalismo"
                },
                "ru": {
                    "id": 151,
                    "langtag": "ru",
                    "title": "минимализм",
                    "slug": "minimalizm"
                },
                "ua": {
                    "id": 151,
                    "langtag": "ua",
                    "title": "мінімалізм",
                    "slug": "minimalizm"
                }
            }
        },
        "category": None,
        "resolution": {
            "id": 79,
            "resolution_group_id": 6,
            "resolution": "3840x2160",
            "public": 1,
            "width": 3840,
            "height": 2160,
            "custom_uri": None,
            "priority": 1,
            "translation": {
                "cn": {
                    "id": 79,
                    "langtag": "cn",
                    "meta_description": "We have picked only best 4K wallpapers and images, so you can be sure that your 4K background would look awesome! Every picture is available for free download without any limitations!",
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                },
                "de": {
                    "id": 79,
                    "langtag": "de",
                    "meta_description": "We have picked only best 4K wallpapers and images, so you can be sure that your 4K background would look awesome! Every picture is available for free download without any limitations!",
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                },
                "en": {
                    "id": 79,
                    "langtag": "en",
                    "meta_description": "We have picked only best 4K wallpapers and images, so you can be sure that your 4K background would look awesome! Every picture is available for free download without any limitations!",
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                },
                "es": {
                    "id": 79,
                    "langtag": "es",
                    "meta_description": "We have picked only best 4K wallpapers and images, so you can be sure that your 4K background would look awesome! Every picture is available for free download without any limitations!",
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                },
                "fr": {
                    "id": 79,
                    "langtag": "fr",
                    "meta_description": "We have picked only best 4K wallpapers and images, so you can be sure that your 4K background would look awesome! Every picture is available for free download without any limitations!",
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                },
                "pt": {
                    "id": 79,
                    "langtag": "pt",
                    "meta_description": "We have picked only best 4K wallpapers and images, so you can be sure that your 4K background would look awesome! Every picture is available for free download without any limitations!",
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                },
                "ru": {
                    "id": 79,
                    "langtag": "ru",
                    "meta_description": None,
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                },
                "ua": {
                    "id": 79,
                    "langtag": "ua",
                    "meta_description": "We have picked only best 4K wallpapers and images, so you can be sure that your 4K background would look awesome! Every picture is available for free download without any limitations!",
                    "meta_title": "4K Ultra HD",
                    "page_description": "3840x2160",
                    "page_name": "4K Ultra HD"
                }
            }
        },
        "topic": None,
        "color": None,
        "search": None,
        "sort": "date",
        # "page": 3,
        "perPage": 30,
        "total": 118,
        "isDefault": False,
        "isExplicitlyVertical": False,
        "pages": 4,
        "sortTypes": [
            "date",
            "popular"
        ],
        "links": {
            "firstPage": "https://wallspic.com/cn/tag/jian_yue/3840x2160",
            "previousPage": "https://wallspic.com/cn/tag/jian_yue/3840x2160",
            "nextPage": "https://wallspic.com/cn/tag/jian_yue/3840x2160?page=3",
            "sort": {
                "date": "https://wallspic.com/cn/tag/jian_yue/3840x2160",
                "popular": "https://wallspic.com/cn/tag/jian_yue/popular/3840x2160"
            }
        }
    }
}
data = json.dumps(data, separators=(',', ':'))
for page in range(2):
    data=json.loads(data)
    data["galleryTarget"]["page"]=page
    data = json.dumps(data)
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    res=response.json()
    count=0
    for link in res["adaptiveGallery"]["list"]:
        links=str(link["thumbnail"]["link"])
        links=links[0:25]+"/attachments/crops"+links[34:-11]+'3840x2160.jpg'
        print(links)
        response = requests.get(links)
        with open(f'./{count}.jpg', 'wb') as f:
            f.write(response.content)
            print("下载成功")
        count+=1

        # print(link["thumbnail"]["link"])

# https://img1.wallspic.com/attachments/crops/6/1/6/4/7/174616/174616-jian_yue-shou_shi-qi_ti-yuan_quan-dian_lan_se_de-3840x2160.jpg