import os
import eel
import csv
import datetime

# P000の初期PWは000b

eel.init("MainProject/view")
eel.start("login.html", block=False)

@eel.expose
def registtData():
    #print(registtDatatoPy())
    try:
        if registtDatatoPy() == True:
            return "tomato"
        else:
            return "onion"
    except(KeyError):
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

#教員ファイル読み込み/tID,tPW照合
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

# reader = "x"

tcName = ["xx", "xx"]
tcDay = [0, 0]
tcPeriod = [0, 0]

@eel.expose
def pickcName():
    global tID
    global tcName
    global tcDay
    global tcPeriod

    # tccsv = [[0] * 5 for i in range(4)]
    # print(tccsv)
    # tcName = [[0] * 5 for i in range(4)]
    # tccsvx = []
    # for i in range(5):
    #     with open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="") as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             print(row)
    #             tanto = str('担当科目' + str(i+1))
    #             print(tanto)
    #             tccsvx[row["ID"]] = row["担当科目1"]
    #         tcName[i] = str(tccsvx[tID])
    #         print("calss1: " + tcName[i])
        

    tc1csv = {}
    tc2csv = {}
    tcName = ["name", "name"]
    with open("./data/教員・担当科目リスト.csv", "r", encoding="utf_8", errors="", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tc1csv[row["ID"]] = row["担当科目1"]
            tc2csv[row["ID"]] = row["担当科目2"]
    tcName[0] = str(tc1csv[tID])
    tcName[1] = str(tc2csv[tID])
    print("calss1: " + tcName[0])
    print("calss2: " + tcName[1])

    # tcID = [[0] * 5 for i in range(4)]
    # tcxID = [[0] * 5 for i in range(4)]
    # for j in range(5):
    #     with open("./data/講義科目ルール.csv", "r", encoding="utf_8", errors="", newline="") as p:
    #         reader = csv.DictReader(p)
    #         for row in reader:
    #             tcxID[j][row["科目名"]] = row["講義ID"]
    #         tcID[j] = str(tcxID[tc1Name])
    #         print("classID: " + tcID[j])


    tc1xID = {}
    tc2xID = {}
    with open("./data/講義科目ルール.csv", "r", encoding="utf_8", errors="", newline="") as p:
        reader = csv.DictReader(p)
        for row in reader:
            tc1xID[row["科目名"]] = row["講義ID"]
            tc2xID[row["科目名"]] = row["講義ID"]
    tc1ID = str(tc1xID[tcName[0]])
    try:
        tc2ID = str(tc2xID[tcName[1]])
    except(KeyError):
        tc2ID = "X0_"
    print("calss1ID: " + tc1ID)
    print("calss2ID: " + tc2ID)

    tcDay = [0, 0]
    tcPeriod = [0, 0]
    cID = [tc1ID, tc2ID]
    for n in range(0, len(cID)):
        # print(n)
        # print(len(cID))
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
            tcDay[n] = ''
            print('Day config error')

        if('12_' in cID[n]):
            tcPeriod[n] = '1,2限'
        elif('23_' in cID[n]):
            tcPeriod[n] = '2,3限'
        elif('34_' in cID[n]):
            tcPeriod[n] = '3,4限'
        elif('45_' in cID[n]):
            tcPeriod[n] = '4,5限'
        elif('1_' in cID[n]):
            tcPeriod[n] = '1限'
        elif('2_' in cID[n]):
            tcPeriod[n] = '2限'
        elif('3_' in cID[n]):
            tcPeriod[n] = '3限'
        elif('4_' in cID[n]):
            tcPeriod[n] = '4限'
        elif('5_' in cID[n]):
            tcPeriod[n] = '5限'
        else:
            tcPeriod[n] = ''
            print('Class period config error')

        try:
            print(tcDay[n] + tcPeriod[n])
        except(TypeError):
            pass
        n = n+1

    tc1Name = tcName[0]
    tc2Name = tcName[1]

    eel.addcData(tc1Name, tc2Name, tcDay, tcPeriod)

#adminでの分岐用
@eel.expose
def clidSet(clid):
    global tcName
    global tcDay
    global tcPeriod

    print(clid)
    print(tcName)
    cDay = "0"
    cPeriod = "0"

    try:
        if clid == "101":
            cConfig = tcName[0]
            cDay = tcDay[0]
            cPeriod = tcPeriod[0]
        elif clid == "102":
            cConfig = tcName[1]
            cDay = tcDay[1]
            cPeriod = tcPeriod[1]
        elif clid == "103":
            cConfig = tcName[2]
            cDay = tcDay[2]
            cPeriod = tcPeriod[2]
        elif clid == "104":
            cConfig = tcName[3]
            cDay = tcDay[3]
            cPeriod = tcPeriod[4]
        elif clid == "105":
            cConfig = tcName[4]
            cDay = tcDay[4]
            cPeriod = tcPeriod[4]
    except(IndexError):
        pass

    print(cConfig)
    tcxID = {}
    tcxCT1 = {}
    tcxCT2 = {}
    tcxLT1 = {}
    tcxLT2 = {}

    with open("./data/講義科目ルール.csv", "r", encoding="utf_8", errors="", newline="") as p:
        reader = csv.DictReader(p)
        for row in reader:
            tcxID[row["科目名"]] = row["講義ID"]
            tcxCT1[row["科目名"]] = row["開始時間"]
            tcxCT2[row["科目名"]] = row["終了時間"]
            tcxLT1[row["科目名"]] = row["出席限度(分)"]
            tcxLT2[row["科目名"]] = row["遅刻限度(分)"]
    tccID = str(tcxID[cConfig])
    tccCT1 = str(tcxCT1[cConfig])
    tccCT2 = str(tcxCT2[cConfig])
    tccLT1 = str(tcxLT1[cConfig])
    tccLT2 = str(tcxLT2[cConfig])
    print("ID:    " + tccID)
    print("Day:   " + cDay)
    print("Period:" + cPeriod)
    print("Start: " + tccCT1)
    print("End:   " + tccCT2)
    print("Limit1:" + tccLT1)
    print("Limit2:" + tccLT2)
    
    eel.initialID(cConfig, tccID, cDay, cPeriod)
    # eel.initialCT(tccCT1, tccCT2)
    # eel.initialLT(tccLT1, tccLT2)
    # return tccCT1, tccCT2, tccLT1, tccLT2

date = str(datetime.date.today())
print(date)

#出席リストCSV作成
@eel.expose
def openIOcsv(cID, cName):
    global date

    stdIDm = stdSim(cID)
    print(stdIDm)

    stdIDx = {}
    stdNamex = {}
    stdID = []
    stdName = []
    print("Preparations are underway: " + cName)
    IOcsvName = "./Mainproject/IOList/" + cName + date + "出欠リスト.csv"
    stdcsvName = "./data/履修者-" + cID + ".csv"
    #履修者のリストを取得
    with open(stdcsvName, "r", encoding="utf_8", errors="", newline="") as stdcsv:
        reader = csv.DictReader(stdcsv)
        for row in reader:
            stdIDx[row["IDm"]] = row["学籍番号"]
            stdNamex[row["IDm"]] = row["名前"]
    for i in range(len(row)):
        try:
            try:
                stdID.append(str(stdIDx[stdIDm[i]]))
                stdName.append(str(stdNamex[stdIDm[i]]))
            except(KeyError):
                stdID.append("S000")
                stdName.append("名無ノ権兵衛")
        except(IndexError):
            pass

    if(os.path.exists(IOcsvName) == False):
        IOcsv = open(IOcsvName, "w", encoding="utf_8")
        IOfieldnames = ["学籍番号", "氏名", "IDm", "入室時刻", "出欠"]
        writer1 = csv.writer(IOcsv)
        writer1.writerow(IOfieldnames)
        os.close
        
    print(stdID)
    print(stdName)

    # for in rangeでstdIDとstdNameをJS関数に投げることで出席
    # 時間は適度な間隔をあけて        

#出席リスト更新

#臨時の出席者
def stdSim(cID):
    print(cID)
    stdIDm = ["012E44A7A518807A", "012E44A7A5187159", "012E44A7A5187429", "012E44A7A5185260"]
    return stdIDm

#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

