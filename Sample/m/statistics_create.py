#作成途中。
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

#カレントディレクトリを指定
path="Sample\m"
os.chdir(path)
#↑CSVファイルが保管されているディレクトリの指定が必要だった

#現在は'no numeric data to plot'というエラーが出現中
data=pd.read_csv("保健体育2021-07-07出欠リスト.csv",encoding='UTF8')
print(data)
#グラフを作成
data.plot()
#棒グラフを作成
#data.plot(kind="bar")
#もしくは
#data.plot.bar()

#棒グラフに使う列を指定
#data[['入室時刻']].plot.bar()
