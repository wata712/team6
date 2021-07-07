#とりあえずひな形だけ作りました。
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

date=pd.read_csv('nanikasira.csv',encoding='UTF8')
date

#棒グラフを作成
date.plot(kind="bar")
#もしくは
date.plot.bar()

#棒グラフに使う列を指定
date[['出席','遅刻','欠席']].plot.bar()
