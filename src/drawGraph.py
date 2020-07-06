import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def drawWordCloud(Word):
    heart_png = np.array(Image.open("./heart.png"))
    wc = WordCloud(font_path="C:/Windows/Fonts/STXINGKA.TTF", background_color="white",
                   mask=heart_png).generate(Word)
    plt.figure()
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("./HotWordCloud.png")
    plt.show()


def drawChart(WordDict):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(8, 6))
    sizes = []
    labels = []
    explode = []
    for key in WordDict:
        labels.append(key)
        sizes.append(WordDict[key])
        explode.append(0.03)
    patches, text1, text2 = plt.pie(sizes, labels=labels, shadow=True, explode=explode,
                            autopct='%3.2f%%', startangle=90, pctdistance=0.6)
    plt.axis('equal')
    plt.legend()
    plt.show()
