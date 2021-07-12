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
        print(atl_header)
        for row in atl_reader:
            data2=row[4]
            count.setdefault(data2,0)
            count[data2] +=1

    with open(atdlist_csvdata,encoding='UTF8') as fc:
        line_count=sum([1 for line in fc])

    li_ct=line_count-1
    print(li_ct)
    for key, value in count.items():
        att_counter='{}: {:d}'.format(key,value)
        print(att_counter)    







#↓memo 後で消す

#os.listdir('保存場所/ディレクトリ名')