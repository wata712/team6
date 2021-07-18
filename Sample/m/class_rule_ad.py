import csv
from types import new_class
import eel
import os
#カレントディレクトリを指定
path="Sample\m"
os.chdir(path)
#classConfig.htmlの入力情報を習得
def get_new_cData():
    new_cData=eel.nw_cDataGet()()
    new_cID=new_cData[0]
    new_cName=new_cData[1]
    new_cDay=new_cData[2]
    new_cStartTime=new_cData[3]
    new_cEndTime=new_cData[4]
    new_cAttendanceLimit=new_cData[5]
    new_cLateLimit=new_cData[6]
    return new_cID,new_cName,new_cDay,new_cStartTime,new_cEndTime,new_cAttendanceLimit,new_cLateLimit

with open('kougi_rule/講義科目ルール.csv','a', encoding="utf_8")as fd:
    csv_add=csv.writer(fd)
    new_class_rule=[]
    #講義ID(1),科目名(2),開始時間(3),終了時間(4),出席限度(分)(5),遅刻限度(分)(6),曜日(7)の順で習得
    nw_cID,nw_cName,nw_stTime,nw_endTime,nw_atdLimit,nw_latLimit,nw_cID=get_new_cData()
    
    #仮入れ
    tID_f='P001'
    tName_f='秋場紀明'
    exam_f='なし'
    regis_f=82

    #講義IDを追加
    new_class_rule.append(nw_cID)
    #講義名を追加
    new_class_rule.append(nw_cName)
    #教師IDを追加
    new_class_rule.append(tID_f)
    #教師名を追加
    new_class_rule.append(tName_f)
    #開始時刻を追加
    new_class_rule.append(nw_stTime)
    #終了時刻を追加
    new_class_rule.append(nw_endTime)
    #出席限度を追加
    new_class_rule.append(nw_atdLimit)
    #遅刻限度を追加
    new_class_rule.append(nw_latLimit)
    #試験有無を追加
    new_class_rule.append(exam_f)
    #履修者数を追加
    new_class_rule.append(regis_f)
    #曜日を追加
    new_class_rule.append(nw_cID)
    #新しい講義情報をリストに追加
    csv_add.writerow(new_class_rule)
    print(csv_add)

eel.init("view")
eel.start("classConfig.html",port=8081)