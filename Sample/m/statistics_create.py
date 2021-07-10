#まだ途中,なんか棒グラフが出ます。
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
import csv

#カレントディレクトリを指定
path="Sample\m"
os.chdir(path)
#↑CSVファイルが保管されているディレクトリの指定が必要だった

#出席,遅刻,欠席のカウント
count = {}
with open("保健体育2021-07-07出欠リスト.csv",encoding='UTF8') as fo:
    atl_reader = csv.reader(fo)
    data=fo
    atl_header = next(atl_reader)
    print(atl_header)
    for row in atl_reader:
       data2=row[4]
       count.setdefault(data2,0)
       count[data2] +=1

with open("保健体育2021-07-07出欠リスト.csv",encoding='UTF8') as fc:
    line_count=sum([1 for line in fc])

li_ct=line_count-1
print(li_ct)   
#カウントを出力
x=[0,1,2]
y_list=[]
x_label=[]
fig=plt.figure()
for key, value in count.items():
   att_counter='{}: {:d}'.format(key,value)
   y_list.append(int(value))
   x_label.append('{}({})'.format(key,value))
   print(att_counter)

print(y_list)
plt.ylim(0,li_ct)
plt.bar(x,y_list)
plt.xticks(x,x_label)    
plt.show()

#各変数の確認用
#print(data2)
#print(atl_reader)
#print(data)
#print(row)   

#plt.plot.bar(value,line_count)
#print(row)
#グラフ保存準備
#fig=plt.figure()
#グラフを作成
#data.plot()
#棒グラフを作成
#data.plot(kind="bar")
#もしくは
#data3.plot.bar()
#棒グラフに使う列を指定
#data2[['出欠']].plot.bar()
