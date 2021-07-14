import csv
import eel
import os
#カレントディレクトリを指定
path="Sample\m"
os.chdir(path)

with open('kougi_rule/講義科目ルール.csv','a', encoding="utf_8")as fd:
    csv_add=csv.writer(fd)

    #csv_add.writerow(ここにリスト型変数)