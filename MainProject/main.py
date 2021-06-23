import eel
import csv

eel.init("MainProject/view")
eel.start("login.html", block=False)

@eel.expose
def registtData():
    #print(registtDatatoPy())
    if registtDatatoPy() == True:
        return "tomato"
    else:
        return "onion"

@eel.expose
def hello():
    print("Hello from Python")

def gettData():
    tData = eel.sendtDatatoPy()()
    gtID = tData[0]
    gtPW = tData[1]
    return gtID, gtPW

tID, tPW = "xxxx", "yyyy"

#main.htmlで入力されたtIDとtPWを照合した先の処理
def registtDatatoPy():
    global tID, tPW
    tID, tPW = gettData()
    print("tID: {0} tPW: {1}".format(tID, tPW))
    if tIDtPWverify(tID,tPW):
        print("Yeeeeeeeeee")
        return True
    else:
        print("Noooooooooo")
        return False

#教員ファイル読み込み/tID,yPW照合
def tIDtPWverify(tID,tPW):
    tID, tPW = gettData()
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
        return True
    else:        
        return False

@eel.expose
def picktName():
    global tID
    tnamecsv = {}
    with open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tnamecsv[row["ID"]] = row["氏名"]
    #print(tnamecsv[tID])
    tName = str(tnamecsv[tID])
    print("user: " + tName)
    eel.printtName(tName)





#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

