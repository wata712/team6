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

#管理モードで教員氏名を表示
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

@eel.expose
def pickcName():
    global tID

    # tccsv = [[0] * 5 for i in range(4)]
    # print(tccsv)
    tcName = [[0] * 5 for i in range(4)]
    tccsvx = []
    for i in range(5):
        with open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                tanto = str('担当科目' + str(i+1))
                print(tanto)
                tccsvx[row["ID"]] = row[tanto]
            tcName[i] = str(tccsvx[tID])
            print("calss1: " + tcName[i])
        

    # tc1csv = {}
    # tc2csv = {}
    # with open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="") as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         tc1csv[row["ID"]] = row["担当科目1"]
    #         tc2csv[row["ID"]] = row["担当科目2"]
    # tc1Name = str(tc1csv[tID])
    # tc2Name = str(tc2csv[tID])
    # print("calss1: " + tc1Name)
    # print("calss2: " + tc2Name)

    tcID = [[0] * 5 for i in range(4)]
    tcxID = [[0] * 5 for i in range(4)]
    for j in range(5):
        with open("./data/講義科目ルール.csv", "r", encoding="utf_8", errors="", newline="") as p:
            reader = csv.DictReader(p)
            for row in reader:
                tcxID[i][row["科目名"]] = row["講義ID"]
            tcID[j] = str(tcxID[tcName[j]])
            print("classID: " + tcID[j])


    # tc1xID = {}
    # tc2xID = {}
    # with open("./data/講義科目ルール.csv", "r", encoding="utf_8", errors="", newline="") as p:
    #     reader = csv.DictReader(p)
    #     for row in reader:
    #         tc1xID[row["科目名"]] = row["講義ID"]
    #         tc2xID[row["科目名"]] = row["講義ID"]
    # tc1ID = str(tc1xID[tc1Name])
    # tc2ID = str(tc2xID[tc2Name])
    # print("calss1ID: " + tc1ID)
    # print("calss2ID: " + tc2ID)

    tcDay = [5]
    tcPeriod = [5]
    cID = [tc1ID, tc2ID]
    for n in range(0, len(cID)):
        print(n)
        print(len(cID))
        if('M' in cID[n]):
            tcDay[n] = '月'
        elif('Tu' in cID[n]):
            tcDay[n] = '火'
        elif('W' in cID[n]):
            tcDay[n] = '水'
        elif('Th' in cID[n]):
            tcDay[n] = '木'
        elif('F' in cID[n]):
            tcDay[n] = '金'
        else:
            print('Day config error')

        if('1' in cID[n]):
            tcPeriod[n] = '1限'
        elif('2' in cID[n]):
            tcPeriod[n] = '2限'
        elif('3' in cID[n]):
            tcPeriod[n] = '3限'
        elif('4' in cID[n]):
            tcPeriod[n] = '4限'
        elif('5' in cID[n]):
            tcPeriod[n] = '5限'
        else:
            print('Class period config error')

        print(tcDay[n] + tcPeriod[n])
        n = n+1


    eel.addcData(tc1Name, tc2Name, tc1ID, tc2ID)


#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

