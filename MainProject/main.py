import eel
import csv

eel.init("MainProject/view")
eel.start("main.html", block=False)

@eel.expose
def registtData(tData):
   tID = tData[0]
   tPW = tData[1]
   print("tID: {0} tPW: {1}".format(tID, tPW))


#教員ファイル読み込み
csv_file = open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="" )
f = csv.DictReader(csv_file)
for row in f:
    #rowはdictionary
    #row["column_name"] or row.get("column_name")で必要な項目を取得することができる
    print(row)

#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

