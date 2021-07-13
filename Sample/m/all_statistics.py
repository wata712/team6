#全体の統計用,とりあえず今は読み込み確認に別のスクリプト入れてます。
from typing import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
import csv
import glob

#カレントディレクトリを指定
path="Sample\m"
os.chdir(path)
#↑CSVファイルが保管されているディレクトリの指定が必要だった

#ディレクトリ内のcsv全部読み1
csv_list2=glob.glob("sample_listbox/*.csv")
for atdlist_csvdata in csv_list2:
    count = {}
    with open(atdlist_csvdata,encoding='UTF8') as fo:
        atl_reader = csv.reader(fo)
        atl_header = next(atl_reader)
        #print(atl_header)
        for row in atl_reader:
            data=row[0]
            data2=row[4]
            count.setdefault(data2,0)
            count[data2] +=1

    with open(atdlist_csvdata,encoding='UTF8') as fc:
        line_count=sum([1 for line in fc])

    li_ct=line_count-1
    #print(li_ct)
    for key, value in count.items():
        att_counter='{}: {:d}'.format(key,value)
        #print(att_counter)    


#こっちに実装用,現在は各生徒ごとに'出席'の数をカウントするようになってます。
csv_list3=glob.glob("sample_listbox/*.csv")
for atdlist_csvdata in csv_list3:
    
    with open(atdlist_csvdata,encoding='UTF8') as f3:
        atl_reader3 = csv.reader(f3)
        atl_header3 = next(atl_reader3)
        #print(atl_header3)
        for row in atl_reader3:
            data=row[0]
            data2=row[4]
            count.setdefault(data,0)
            if '出席' in data2:
                count[data] +=1
    alatd_list=[]

    stnumb_list=[]
    atd_count_list=[]
    list_length=len(stnumb_list)

    for key, value in count.items():
        att_counter='{}: {:d}'.format(key,value)
        #学番と出席数リスト
        alatd_list.append(att_counter)
        #学番リスト
        stnumb_list.append('{}'.format(key))
        #出席数リスト
        atd_count_list.append(int(value))

#人数
list_length=len(stnumb_list)-1
#print(list_length)

#リストの先頭('出席'と出席数)を削除
stnumb_list.remove('出席')
atd_count_list.remove(list_length)

#print(alatd_list)
print(stnumb_list)
print(atd_count_list)

#↓ここから横棒グラフ作成
fig=plt.figure()
y_set=list(range(list_length))
#print(y_set)    





#↓memo 後で消す

#os.listdir('保存場所/ディレクトリ名')