import TopGet
import Analyze
import drawGraph
import save


if __name__ == '__main__':
    HotList = TopGet.topSummaryGet()
    WeiboList, ZhihuList = Analyze.cutWord(HotList)
    # save.updateHotList2CSV(WeiboList, ZhihuList)
    # drawGraph.drawWordCloud("孟美琪 孙如云 李梓萌 张帆 徐浩泽 孟美琪 孟美琪 孟美琪 李梓萌 "
    #                         "李梓萌 张帆 吴亦凡 掌翼龙 孙哥 李哥 仲菲菲 仲菲菲 仲菲菲 "
    #                         "张杰 张艺凡 谢安诗")
    # chart = {"孟美琪": 5, "孙如云": 3, "李梓萌": 2, "徐浩泽": 4, "吴亦凡": 7}
    # drawGraph.drawChart(chart)
