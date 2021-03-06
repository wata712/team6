#全体の統計用,とりあえず今は読み込み確認に別のスクリプト入れてます。
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
count1 = {}
for atdlist_csvdata in csv_list3:
    
    with open(atdlist_csvdata,encoding='UTF8') as f3:
        atl_reader3 = csv.reader(f3)
        atl_header3 = next(atl_reader3)
        #print(atl_header3)
        for row in atl_reader3:
            data=row[0]
            data2=row[4]
            count1.setdefault(data,0)
            if '出席' in data2:
                count1[data] +=1
    
    #alatd_list=[]
    stnumb_list=[]
    atd_count_list=[]
    

    for key1, value1 in count1.items():
        att_counter='{}: {:d}'.format(key1,value1)
        #学番と出席数リスト
        #alatd_list.append(att_counter)
        #学番リスト
        stnumb_list.append('{}'.format(key1))
        #出席数リスト
        atd_count_list.append(int(value1))
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
        stnumb_list2.append('{}'.format(key2))
        #出席数リスト
        atd_count_list2.append(int(value2))
    #print(stnumb_list)
    #print(atd_count_list)
count3 = {}
for atdlist_csvdata in csv_list3:
    
    with open(atdlist_csvdata,encoding='UTF8') as f5:
        atl_reader5 = csv.reader(f5)
        atl_header5 = next(atl_reader5)
        #print(atl_header3)
        for row in atl_reader5:
            data5=row[0]
            data6=row[4]
            count3.setdefault(data5,0)
            if '欠席' in data6:
                count3[data5] +=1
    
    #alatd_list=[]
    stnumb_list3=[]
    atd_count_list3=[]
    

    for key3, value3 in count3.items():
        att_counter3='{}: {:d}'.format(key3,value3)
        #学番と出席数リスト
        #alatd_list.append(att_counter)
        #学番リスト
        stnumb_list3.append('{}'.format(key3))
        #出席数リスト
        atd_count_list3.append(int(value3))
    print(stnumb_list3)
    print(atd_count_list)
#人数
list_length=len(stnumb_list)
print(list_length)

#リストの先頭('出席'と出席数)を削除
#stnumb_list.remove('出席')

#atd_count_list.remove(list_length)


#print(alatd_list)
#print(stnumb_list)
#print(atd_count_list)
#print(stnumb_list2)
#print(atd_count_list2)

#↓ここから棒グラフ作成
fig=plt.figure()
#学生の数,0から連続した整数のリスト
y_set=list(range(list_length))

graph1=plt.bar(y_set,atd_count_list,align="edge",width=-0.5,color="green",label="出席")
graph2=plt.bar(y_set,atd_count_list2,align="center",width=0.5,color="blue",label="遅刻")
graph3=plt.bar(y_set,atd_count_list3,align="edge",width=0.5,color="red",label="欠席")
plt.xticks(y_set,stnumb_list,rotation=90)
plt.legend()
plt.show()