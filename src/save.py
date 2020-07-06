import pandas as pd


def updateHotList2CSV(WeiboWordList, ZhihuWordList):
    csvFile = pd.read_csv("../docs/HotList.csv")

