import eel
import csv
from datetime import datetime as dt

eel.init("view") #HTMLのフォルダ
eel.start("main.html",block=False, port=9999) #スタートページのファイル名

@eel.expose
def hello():
   print("Hello World!")

'''
@eel.expose
def send(tID,tPW):
   print("tID: {}".format(tID))
   print("tPW: {}".format(tPW))
   return "ok"
'''

@eel.expose
def registtData():
   #tID = tData[0]
   #tPW = tData[1]
   print("tID: ")
   #print("tPW: {}".format(tPW))

'''
.format(textbox1)
while True:
   timestamp = dt.now()
   eel.addText("The time now is {}".format(timestamp.strftime("%I:%M:%S %p")))

   eel.sleep(1.0)
'''

#教員ファイル読み込み
csv_file = open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="" )
f = csv.DictReader(csv_file)
for row in f:
    #rowはdictionary
    #row["column_name"] or row.get("column_name")で必要な項目を取得することができる
    print(row)