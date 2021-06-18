import eel
import csv

eel.init("MainProject/view")
eel.start("main.html", block=False)

@eel.expose
def registtData():
   registtDatatoPy()

def registtDatatoPy():
    tData = eel.sendtDatatoPy()()
    tID = tData[0]
    tPW = tData[1]
    print("tID: {0} tPW: {1}".format(tID, tPW))
    tIDtPWverify(tID,tPW)

#教員ファイル読み込み/tID,yPW照合
def tIDtPWverify(tID,tPW):
    tnamecsv = {}
    with open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tnamecsv[row["ID"]] = row["氏名"]
    print(tnamecsv[tID])

    tpwcsv = {}
    with open("./data/tPW.csv","r")as p:
        reader = csv.DictReader(p)
        for prow in reader:
            tpwcsv[prow["tID"]] = prow["tPW"]
        tPWoncsv = tpwcsv[tID]
    #print(tPWoncsv)

    if tPW == tPWoncsv:
        print("Yeeeeeeeeee")
        return True
    else:
        print("noooooooooo")
        return False

    






#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

