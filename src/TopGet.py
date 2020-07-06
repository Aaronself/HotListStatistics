import requests
import re
from bs4 import BeautifulSoup
import numpy as np


def topSummaryGet():
    WeiboTopSummaryUrl = "https://s.weibo.com/top/summary?"
    ZhihuTopSummaryUrl = "https://www.zhihu.com/billboard"
    WeiboTopList = getWeiBoTopList(WeiboTopSummaryUrl)
    ZhihuTopList = getZhihuTopList(ZhihuTopSummaryUrl)
    HotList = {}
    HotList["Weibo"] = WeiboTopList
    HotList["Zhihu"] = ZhihuTopList
    return HotList


def getTopSummaryHTML(TopSummaryUrl, data, cookies, headers):
    try:
        r = requests.get(TopSummaryUrl, params=data, cookies=cookies, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error")


def getWeiBoTopList(TopSummaryUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36'}
    data = {'cate': 'realtimehot'}
    cookies = {}
    # with open('./cookie.txt', 'r', encoding='utf-8') as f:
    #     name, value = f.readline().strip().split("=", 1)
    #     cookies[name] = value
    TopList = {}
    TopNameList = []
    TopHotList = []
    html = getTopSummaryHTML(TopSummaryUrl, data, cookies, headers)
    soup = BeautifulSoup(html, 'lxml')
    label_a = soup.find_all('a')
    for i in label_a:
        try:
            href = i.attrs['href']
            if re.findall(r"^\/weibo\?q=.*", href)[0]:
                TopNameList.append(str(i.string))
        except:
            continue
    label_span = soup.find_all('span')
    for i in label_span:
        try:
            string = i.string
            if re.findall(r"^[0-9]*", string)[0]:
                TopHotList.append(str(string))
        except:
            continue
    if len(TopNameList) == 51:
        TopList[TopNameList[0]] = "Top"
        for i in range(len(TopHotList)):
            TopList[TopNameList[i + 1]] = TopHotList[i]
    elif len(TopNameList) == 50:
        for i in range(len(TopHotList)):
            TopList[TopNameList[i]] = TopHotList[i]

    return TopList


def getZhihuTopList(TopSummaryUrl):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    data = {}
    cookies = {}
    TopList = {}
    TopNameList = []
    TopHotList = []
    html = getTopSummaryHTML(TopSummaryUrl, data, cookies, headers)
    soup = BeautifulSoup(html, 'lxml')
    label_a = soup.find_all("a")
    for i in label_a:
        try:
            text = i.get_text()[2:]
            TopNameList.append(str(text.split("？")[0]))
            TopHotList.append(str(text.split("？")[1]))
        except:
            continue
    for i in range(len(TopHotList)):
        TopList[TopNameList[i]] = TopHotList[i]

    return TopList
