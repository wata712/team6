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

#各生徒ごとに'出席'の数をカウント
csv_list3=glob.glob("sample_listbox/*.csv")
count = {}
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
    
    #alatd_list=[]
    stnumb_list=[]
    atd_count_list=[]
    

    for key, value in count.items():
        att_counter='{}: {:d}'.format(key,value)
        #学番と出席数リスト
        #alatd_list.append(att_counter)
        #学番リスト
        stnumb_list.append('{}'.format(key))
        #出席数リスト
        atd_count_list.append(int(value))
    #print(stnumb_list)
    #print(atd_count_list)

count2 = {}
for atdlist_csvdata in csv_list3:
    
    with open(atdlist_csvdata,encoding='UTF8') as f4:
        atl_reader4 = csv.reader(f4)
        atl_header4 = next(atl_reader4)
        #print(atl_header3)
        for row in atl_reader4:
            data3=row[0]
            data4=row[4]
            count2.setdefault(data3,0)
            if '遅刻' in data4:
                count2[data3] +=1
    
    #alatd_list=[]
    stnumb_list2=[]
    atd_count_list2=[]
    

    for key2, value2 in count2.items():
        att_counter2='{}: {:d}'.format(key2,value2)
        #学番と出席数リスト
        #alatd_list.append(att_counter)
        #学番リスト
        stnumb_list2.append('{}'.format(key))
        #出席数リスト
        atd_count_list2.append(int(value2))
    #print(stnumb_list)
    #print(atd_count_list)
#人数
list_length=len(stnumb_list)
print(list_length)

#リストの先頭('出席'と出席数)を削除
#stnumb_list.remove('出席')

#atd_count_list.remove(list_length)


#print(alatd_list)
print(stnumb_list)
print(atd_count_list)
print(stnumb_list2)
print(atd_count_list2)

#↓ここから横棒グラフ作成
fig=plt.figure()
#学生の数,0から連続した整数のリスト
y_set=list(range(list_length))

#print(y_set)
graph1=plt.barh(y_set,atd_count_list,height=0.3,color="green")


plt.yticks(y_set,stnumb_list)
plt.show()