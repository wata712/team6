import csv
from types import new_class
import eel
import os
#カレントディレクトリを指定
path="Sample\m"
os.chdir(path)
#該当箇所には一旦inputを保存(後でeel.honyara()みたいなのにつなげる)
with open('kougi_rule/講義科目ルール.csv','a', encoding="utf_8")as fd:
    csv_add=csv.writer(fd)
    new_class_rule=[]
    #講義ID(1),科目名(2),ID,教員名,開始時間(3),終了時間(4),出席限度(分)(5),遅刻限度(分)(6),試験,履修者数,曜日(7)
    #講義ID(1)
    nw_cID=input('講義IDを入力:')
    new_class_rule.append(nw_cID)
    #科目名(2)
    nw_cName=input('科目名を入力:')
    new_class_rule.append(nw_cName)
    #仮入れ1
    tID_f='P001'
    new_class_rule.append(tID_f)
    tName_f='秋場紀明'
    new_class_rule.append(tName_f)
    #開始時間(3)
    nw_stTime=input('開始時間を入力:')
    new_class_rule.append(nw_stTime)
    #終了時間(4)
    nw_fiTime=input('終了時間を入力:')
    new_class_rule.append(nw_fiTime)
    #出席限度(分)(5)
    nw_atdLimit=input('出席限度を入力:')
    new_class_rule.append(nw_atdLimit)
    #遅刻限度(分)(6)
    nw_latLimit=input('遅刻限度を入力:')
    new_class_rule.append(nw_latLimit)
    #仮入れ2
    exam_f='なし'
    new_class_rule.append(exam_f)
    regis_f=82
    new_class_rule.append(regis_f)
    #曜日(7)
    nw_cDate=input('曜日を入力:')
    new_class_rule.append(nw_cDate)
    csv_add.writerow(new_class_rule)
    print(csv_add)
#eel.init("Sample/m/view")
#eel.start("classConfig.html",port=8081)