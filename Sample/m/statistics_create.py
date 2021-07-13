#まだ途中,欠席がいないときにも対応しました。
from typing import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
import csv
import os.path

#カレントディレクトリを指定
path="Sample\m"
os.chdir(path)
#↑CSVファイルが保管されているディレクトリの指定が必要だった

file_path="sample_listbox/保健体育2021-07-07出欠リスト.csv"
file_name_path=os.path.basename(file_path)
#出席,遅刻,欠席のカウント
count = {}
with open("sample_listbox/保健体育2021-07-07出欠リスト.csv",encoding='UTF8') as fo:
    atl_reader = csv.reader(fo)
    atl_header = next(atl_reader)
    data=fo
    print(atl_header)
    for row in atl_reader:
       data2=row[4]
       count.setdefault(data2,0)
       count[data2] +=1

with open("sample_listbox/保健体育2021-07-07出欠リスト.csv",encoding='UTF8') as fc:
    line_count=sum([1 for line in fc])

li_ct=line_count-1
print(li_ct)
y_list=[]
x_label=[]
fig=plt.figure()
plt.title(file_name_path)
for key, value in count.items():
   att_counter='{}: {:d}'.format(key,value)
   #y軸設定用
   y_list.append(int(value))
   #x軸の文字ラベル用
   x_label.append('{}'.format(key))

#ここでy軸を降順にソート
y_list2=sorted(y_list,reverse=True)

#'遅刻''欠席'が一人もいないとき用の処理(y軸用)
if len(y_list2)==2:
    y_list2.append(0)
    #要素が2つのとき
elif len(y_list2)==1:
    y_list2.append(0)
    y_list2.append(0)
    #要素が1つのとき
else:
    y_list2
    #要素が3つのとき

x=[0,1,2]

#このex_labelで出席遅刻欠席の順番を指定
ex_label=['出席','遅刻','欠席']

#'遅刻''欠席'が一人もいないとき用の処理(x軸用)
if len(x_label)==2:
    if '出席' in x_label:
        if '遅刻' in x_label:
            x_label.append('欠席')
            #'欠席'がないとき
        else:
            x_label.append('遅刻')
            #'遅刻'がないとき
    else:
        x_label.append('出席')
        #'出席'がないとき　←この場合はいらないとは思うが例外から外すために記載
    #要素が2つのとき    
elif len(x_label)==1:
    if '出席' in x_label:
        x_label.append('遅刻')
        x_label.append('欠席')
        #'遅刻','欠席'がないとき
    elif '遅刻' in x_label:
        x_label.append('出席')
        x_label.append('欠席')
        #'出席''欠席'がないとき
    else:
        x_label.append('出席')
        x_label.append('遅刻')
        #'出席''遅刻'がないとき ←この場合はいらないとは思うが例外から外すために記載2
else:
    x_label

x_label2=sorted(x_label,key=ex_label.index)



#↓棒グラフ作成
print(y_list2)
print(x_label2)
plt.ylim(0,li_ct)
graph=plt.bar(x,y_list2)

height=y_list2
for rect in graph:
    height=rect.get_height()
    plt.annotate('{}'.format(height),xy=(rect.get_x() + rect.get_width()/2,height),xytext=(0,3),textcoords="offset points",ha='center',va='bottom')

plt.xticks(x,x_label2)    
plt.show()
#ここまでが一つの出席リストをグラフ化するスクリプト


#↓memo 後で消す

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
