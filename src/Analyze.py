import jieba
import jieba.analyse


def cutWord(HotList):
    WeiboWordList = []
    ZhihuWordList = []
    jieba.load_userdict("../docs/self-built-dict.txt")
    WeiboList = HotList['Weibo']
    ZhihuList = HotList['Zhihu']
    if len(WeiboList):
        for key in WeiboList:
            seg_list = jieba.analyse.extract_tags(key, topK=3, allowPOS=('n', 'nr', 'ns', 'v'))
            WeiboWordList.append(seg_list)
        print(WeiboWordList)
    else:
        print("weibo wrong!")

    if len(ZhihuList):
        for key in ZhihuList:
            seg_list = jieba.analyse.extract_tags(key, topK=3, allowPOS=('n', 'nr', 't', 'v'))
            ZhihuWordList.append(seg_list)
    else:
        print("zhihu wrong!")
    return WeiboWordList, ZhihuWordList

