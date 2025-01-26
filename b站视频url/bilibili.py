import csv
import requests

url="https://api.bilibili.com/x/web-interface/wbi/search/type?category_id=&search_type=video&ad_resource=5654&__refresh__=true&_extra=&context=&page={}&page_size=42&pubtime_begin_s=0&pubtime_end_s=0&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E6%90%9E%E7%AC%91%E8%A7%86%E9%A2%91&qv_id=RAB4nR25f6ou3mmWEewlhD68eLWyDbMb&source_tag=3&gaia_vtoken=&dynamic_offset=60&web_location=1430654&w_rid=c7916248dda36c1284305b77635cc7e1&wts=1734868199"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.9101 SLBChan/105 SLBVPV/64-bit",
    "Cookie":"buvid3=087E8BE9-462A-FA77-D3CD-A53BE4FDB90340812infoc; b_nut=1732580240; _uuid=455691EB-21BA-B9F1-9A94-E10F7109CA5B6B42672infoc; buvid_fp=1d99c84d6d4aa9ed4407f06256a60651; buvid4=4EDA99A8-6DEA-2F72-8732-AA8EE61EE83535705-024112600-WCeJNud9XW4ixTBijMjL9F432KpE/8s/zkzoz4kaT1mN1IIt9cv77yPCxZSYxXVV; rpdid=0zbfAGu7i0|non3o6gF|1B8|3w1TfJlm; header_theme_version=CLOSE; enable_web_push=DISABLE; home_feed_column=4; is-2022-channel=1; browser_resolution=1232-177; b_lsid=957C4CFE_193EE3330F9; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUxMjczNTMsImlhdCI6MTczNDg2ODA5MywicGx0IjotMX0.Um9TCaLuM34umNbwP7R25bv_FScWGtwRD9bwvbLtleg; bili_ticket_expires=1735127293; CURRENT_FNVAL=2000; sid=84np2t1o",
    "Referer":"https://search.bilibili.com/video?"
}
with open("bilibili_video_url.csv","a",encoding="utf-8",newline="") as f:
    f_name=["author","name","url"]
    f_video=csv.DictWriter(f,fieldnames=f_name)
    f_video.writeheader()
    for page in range(2,3):
        response = requests.get(url.format(page), headers=headers).json()
        for result1 in response["data"]["result"]:
            items=dict()
            items["author"]=result1["author"]
            items["name"]=result1["title"]
            items["url"]=result1["arcurl"]
            f_video.writerow(items)