### Team6 main.py ###
### ブラウザウィンドウの推奨アスペクト比 4:3 または 16:9 または 21:9 ###

import os
from re import S
from subprocess import NORMAL_PRIORITY_CLASS
from time import time
from bottle import WSGIHeaderDict
import eel
import csv
import sys
import operator
import datetime
import numpy
import random
# import importer
# import exporter

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

#仮の出席者
def stdSim(cID):
    number=range(1,101)
    rnumber=random.sample(number,len(number)) #学籍番号を(ランダムに)生成
    temlist=[]
    for i in rnumber:
        temNo= "S{:0>3}".format(i)  #"S001" "S012"のように3桁表示
        temlist.append(temNo) #temlistはS001からS100の100個の要素からなるリスト

    #講義IDに一致した履修者csvを開く
    stdIDmx = {} #辞書型
    stdIDm = [] #配列
    stdcsvName = "./data/履修者-" + cID + ".csv"
    with open(stdcsvName, "r", encoding="utf_8", errors="", newline="") as p:
        reader = csv.DictReader(p)
        for row in reader:
            stdIDmx[row["学籍番号"]] = row["IDm"]
        for i in range(len(temlist)):
            try:
                IDm = str(stdIDmx[temlist[i]])
                stdIDm.append(IDm)
            except KeyError:
                pass
            
    # print(stdcsvName)
    # print(len(stdIDm))
    return stdIDm

IOcsvName = "xx"

#出席リストCSV作成
@eel.expose
def openIOcsv(cID, cName):
    global date
    global IOcsvName

    stdIDm = stdSim(cID)
    # print(stdIDm)

    stdIDx = {}
    stdNamex = {}
    stdID = []
    stdName = []
    print("Preparations are underway: " + cName)
    dirName = "./Mainproject/IOList/" + cName
    IOcsvName = "./Mainproject/IOList/" + cName + "/" + cName + date + "出欠リスト.csv"
    stdcsvName = "./data/履修者-" + cID + ".csv"
    if(os.path.exists(dirName) == False):
        os.mkdir(dirName)
    #履修者のリストを取得
    with open(stdcsvName, "r", encoding="utf_8", errors="") as stdcsv:
        reader = csv.DictReader(stdcsv)
        for row in reader:
            stdIDx[row["IDm"]] = row["学籍番号"]
            stdNamex[row["IDm"]] = row["名前"]
    print("履修者数: " + str(len(stdIDm)))
    for i in range(len(stdIDm)):
        try:
            try:
                stdID.append(str(stdIDx[stdIDm[i]]))
                stdName.append(str(stdNamex[stdIDm[i]]))
            except(KeyError):
                stdID.append("S000")
                stdName.append("名無ノ権兵衛")
        except(IndexError):
            pass

    #初期出欠リストcsv作成
    if(os.path.exists(IOcsvName) == False):
        with open(IOcsvName, "w", encoding="utf_8", newline="") as IOcsv:
            writer = csv.writer(IOcsv)
            writer.writerow(["学籍番号", "名前", "IDm", "入室時刻", "出欠"])
            for k in range(len(stdIDm)):
                writer.writerow([stdID[k], stdName[k], stdIDm[k], "00:00:00", "欠席"])

        # ソート
        with open(IOcsvName, "r", encoding="utf_8") as IOcsvs:
            reader = csv.DictReader(IOcsvs)
            IOdict = []
            for row in reader:
                IOdict.append(row)
            sortedIOdict = sorted(IOdict, key=lambda x:x["学籍番号"])

        with open(IOcsvName, "w", encoding="utf_8", newline="") as IOcsvw:
            writer2 = csv.writer(IOcsvw)
            writer2.writerow(["学籍番号", "名前", "IDm", "入室時刻", "出欠"])
            for g in range(len(stdIDm)):
                dictvalues = sortedIOdict[g].values()
                writer2.writerow(dictvalues)


    # print(stdID)
    # print(stdName)

    # for in rangeでstdIDとstdNameをJS関数に投げることで出席
    # 適度な間隔をあけて

    # カードタッチ間隔
    timespanx = numpy.random.normal(
        loc = 7,                    # 平均
        scale = (len(stdIDm)/6),    # 標準偏差
        size = len(stdIDm)          # 出力配列のサイズ
    )
    timespan = timespanx
    tmp = 0
    for j in range(len(timespanx)):
        timespan[j] = int(timespan[j])
        tmp = tmp + timespan[j]
    # print(timespan)
    print(tmp/60)

    #出席リスト更新
    def touchIDcard(no):
        dtNow = datetime.datetime.now()
        now = str(dtNow.time())[0:8]
        print(now)
        eel.showIDinfo(stdID[no], stdName[no])

        # with open(IOcsvName, "w", encoding="utf_8", newline="") as IOcsvw:
        #     writer2 = csv.writer(IOcsvw)
        #     writer2.writerow(["学籍番号", "名前", "IDm", "入室時刻", "出欠"])
        #     for g in range(len(stdIDm)):
        #         dictvalues = sortedIOdict[g].values()
        #         writer2.writerow(dictvalues)


        stdInTimex = {}
        stdIOx = {}
        stdInTime = []
        stdIO = []

        # lst = []
        with open(IOcsvName, "a", encoding="utf_8", errors="", newline="") as IOcsva:
        #     readera = csv.reader(stdcsva)
        #     lst = [r for r in readera]
        # IOdata = ([stdID[no], stdName[no], stdIDm[no], now, "出席"])
        # for row in lst:
        #     if row[0] == stdID[no]:
        #         row.clear()
        #         row.extend(IOdata)

            readera = csv.DictReader(IOcsva)
            for row in readera:
                stdInTimex[row["学籍番号"]] = row["入室時刻"]
                stdIOx[row["学籍番号"]] = row["出欠"]
        for v in range(len(row)):
            if v == no:
                

                stdInTime = str(stdInTimex[stdID[v]])
                stdIO = str(stdIOx[stdID[v]])
        print(stdInTime)
        print(stdIO)

        # with open(IOcsvName, "w", encoding="utf_8", errors="", newline="") as IOcsvc:
        #     writer3 = csv.writer(IOcsvc)

    # タッチのトリガー
    eel.sleep(3)
    for s in range(len(stdIDm)):
        if s != (len(stdIDm)-1):
            if timespan[s]<=0:
                timespan[s] = (timespan[s] * -1) + 1
            print(timespan[s], end=" ")
            print(stdIDm[s])
            touchIDcard(s)
            eel.sleep(timespan[s])
        else:
            # 遅刻ちゃん
            num = random.randint(0,9)
            print(num)
            if num > 8:
                eel.sleep(800)
            elif num > 7:
                eel.sleep(300)
            elif num > 4:
                eel.sleep(60)
            else:
                eel.sleep(3)
            print(stdIDm[s])
            touchIDcard(s)

    



@eel.expose
def generateIOcsvName(clid):
    global tcName
    try:
        if clid == "101":
            cName = tcName[0]
        elif clid == "102":
            cName = tcName[1]
        elif clid == "103":
            cName = tcName[2]
        elif clid == "104":
            cName = tcName[3]
        elif clid == "105":
            cName = tcName[4]
    except(IndexError):
        pass

    IOcsvName = "./Mainproject/IOList/" + cName + "/" + cName + date + "出欠リスト.csv"
    print(IOcsvName)
    eel.getIOcsvName(IOcsvName)





#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

