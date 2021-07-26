### Team6 main.py ###
### author: tanahashi, kurita, ito ###

import os
import eel
import csv
import datetime
from datetime import datetime as dt
import numpy
import random
import matplotlib.pyplot as plt
import japanize_matplotlib # グラフの日本語表示に必要
from typing import Counter

# import importer
# import exporter

# P000の初期PWは000b
japanize_matplotlib

print("バックグラウンドで port=8000 が使用されていると正常に動作しません。")

cwd = os.getcwd()
xcwd = cwd.replace('\\','/')

vcwd = xcwd + "/view"
dcwd = xcwd + "/data"
IOcwd = xcwd + "/IOList"
print(vcwd)

eel.init(vcwd)
eel.start("login.html", size=(800, 480), block=False)

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
    global dcwd
    ktcwd = dcwd + "/教員・担当科目リスト.csv"
    tPWcwd = dcwd + "/tPW.csv"
    tID, tPW = gettData()
    tnamecsv = {}
    with open(ktcwd, "r", encoding="utf_8", errors="", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tnamecsv[row["ID"]] = row["氏名"]
    print(tnamecsv[tID])

    tpwcsv = {}
    with open(tPWcwd,"r")as p:
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
    global dcwd
    ktcwd = dcwd + "/教員・担当科目リスト.csv"
    try:
        global tID
        tnamecsv = {}
        with open(ktcwd, "r", encoding="utf_8", errors="", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tnamecsv[row["ID"]] = row["氏名"]
        #print(tnamecsv[tID])
        tName = str(tnamecsv[tID])
        print("user: " + tName)
        eel.printtName(tName)
    except(FileNotFoundError):
        os.getcwd()
        os.chdir(xcwd) 
        picktName()

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
    global dcwd
    ktcwd = dcwd + "/教員・担当科目リスト.csv"
    crcwd = dcwd + "/講義科目ルール.csv"
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
    with open(ktcwd, "r", encoding="utf_8", errors="", newline="") as f:
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
    with open(crcwd, "r", encoding="utf_8", errors="", newline="") as p:
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
            tcName[1] = "undefined"
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
        except(IndexError):
            pass
        n = n+1

    tc1Name = tcName[0]
    tc2Name = tcName[1]

    tclen = len(tcName)
    tclen = 5

    eel.addcData(tcName, tclen, tcDay, tcPeriod)

#adminでの分岐用
@eel.expose
def clidSet(clid):
    global tcName
    global tcDay
    global tcPeriod
    global dcwd
    crcwd = dcwd + "/講義科目ルール.csv"

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

    with open(crcwd, "r", encoding="utf_8", errors="", newline="") as p:
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

    tccCT1 = str(tcxCT1[cConfig])
    tccCT2 = str(tcxCT2[cConfig])
    tccLT1 = str(tcxCT1[cConfig][0:5])
    tccLT2 = str(tcxCT1[cConfig][0:5])
    
    tcxLT1m = int(tcxLT1[cConfig])
    tcxLT2m = int(tcxLT2[cConfig])

    # tcxLT1m = dt.strptime(tcxLT1m, '%H:%M:%S')
    # tcxLT2m = dt.strptime(tcxLT2m, '%H:%M:%S')

    tccCT1t = dt.strptime(tccCT1, '%H:%M')
    tccCT2t = dt.strptime(tccCT2, '%H:%M')
    tccLT1t = dt.strptime(tccLT1, '%H:%M')
    tccLT2t = dt.strptime(tccLT2, '%H:%M')

    tccLT1t = tccLT1t + datetime.timedelta(minutes=tcxLT1m)
    tccLT2t = tccLT2t + datetime.timedelta(minutes=tcxLT2m)

    tccCT1 = str(tccCT1t.time())
    tccCT2 = str(tccCT2t.time())
    tccLT1 = str(tccLT1t.time())
    tccLT2 = str(tccLT2t.time())

    tccCT1 = tccCT1[0:5]
    tccCT2 = tccCT2[0:5]
    tccLT1 = tccLT1[0:5]
    tccLT2 = tccLT2[0:5]

    print("授業開始: " + tccCT1)
    print("授業終了: " + tccCT2)
    print("以降遅刻: " + tccLT1)
    print("以降欠席: " + tccLT2)
    
    eel.initialID(cConfig, tccID, cDay, cPeriod, tccCT1, tccCT2, tccLT1, tccLT2)
    # eel.initialCT(tccCT1, tccCT2)
    # eel.initialLT(tccLT1, tccLT2)
    # return tccCT1, tccCT2, tccLT1, tccLT2

datew = datetime.date.today()
datew = datew.strftime("%Y_%m_%d")
print(datew)

# 仮の出席者
# main author: ito
def stdSim(cID):
    global dcwd
    rcwd = dcwd + "/履修者-"

    number=range(1,101)
    rnumber=random.sample(number,len(number)) #学籍番号を(ランダムに)生成
    temlist=[]
    for i in rnumber:
        temNo= "S{:0>3}".format(i)  #"S001" "S012"のように3桁表示
        temlist.append(temNo) #temlistはS001からS100の100個の要素からなるリスト

    #講義IDに一致した履修者csvを開く
    stdIDmx = {} #辞書型
    stdIDm = [] #配列
    stdcsvName = rcwd + cID + ".csv"
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

#出欠リストCSV操作 兼 出席シミュレータ
@eel.expose
def openIOcsv(cID, cName):
    global datew
    global IOcsvName
    global dcwd
    global IOcwd
    crcwd = dcwd + "/講義科目ルール.csv"
    rcwd = dcwd + "/履修者-"
    
    tcxCT1 = {}
    tcxCT2 = {}
    tcxLT1 = {}
    tcxLT2 = {}

    with open(crcwd, "r", encoding="utf_8", errors="", newline="") as p:
        reader = csv.DictReader(p)
        for row in reader:
            tcxCT1[row["科目名"]] = row["開始時間"]
            tcxCT2[row["科目名"]] = row["終了時間"]
            tcxLT1[row["科目名"]] = row["出席限度(分)"]
            tcxLT2[row["科目名"]] = row["遅刻限度(分)"]
    tccCT1 = str(tcxCT1[cName]) + ":00"
    tccCT2 = str(tcxCT2[cName]) + ":00"
    tccLT1 = str(tcxCT1[cName][0:5]) + ":00"
    tccLT2 = str(tcxCT1[cName][0:5]) + ":00"
    
    tcxLT1m = int(tcxLT1[cName])
    tcxLT2m = int(tcxLT2[cName])

    # tcxLT1m = dt.strptime(tcxLT1m, '%H:%M:%S')
    # tcxLT2m = dt.strptime(tcxLT2m, '%H:%M:%S')

    tccCT1t = dt.strptime(tccCT1, '%H:%M:%S')
    tccCT2t = dt.strptime(tccCT2, '%H:%M:%S')
    tccLT1t = dt.strptime(tccLT1, '%H:%M:%S')
    tccLT2t = dt.strptime(tccLT2, '%H:%M:%S')

    tccLT1t = tccLT1t + datetime.timedelta(minutes=tcxLT1m)
    tccLT2t = tccLT2t + datetime.timedelta(minutes=tcxLT2m)

    tccCT1t = tccCT1t.time()
    tccCT2t = tccCT2t.time()
    tccLT1t = tccLT1t.time()
    tccLT2t = tccLT2t.time()

    print("授業開始: " + str(tccCT1t))
    print("授業終了: " + str(tccCT2t))
    print("以降遅刻: " + str(tccLT1t))
    print("以降欠席: " + str(tccLT2t))

    LimitTime = [tccCT1t, tccCT2t, tccLT1t, tccLT2t]

    stdIDm = stdSim(cID)
    # print(stdIDm)

    stdIDx = {}
    stdNamex = {}
    stdID = []
    stdName = []
    print("Preparations are underway: " + cName)
    dirName = IOcwd + "/" + cName
    IOcsvName = IOcwd + "/" + cName + "/" + cName + datew + "出欠リスト.csv"
    stdcsvName = rcwd + cID + ".csv"
    if(os.path.exists(dirName) == False):
        os.mkdir(dirName)
    #履修者のリストを取得
    with open(stdcsvName, "r", encoding="utf_8", errors="") as stdcsv:
        reader = csv.DictReader(stdcsv)
        for row in reader:
            stdIDx[row["IDm"]] = row["学籍番号"]
            stdNamex[row["IDm"]] = row["名前"]
    stdlen = len(stdIDm)
    print("履修者数: " + str(stdlen))
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
    def touchIDcard(no, stdlenx, LimitTime):
        dtNow = datetime.datetime.now()
        now = dtNow.time()
        print(now)

        status = "出席"

        if now < LimitTime[2]:
            status = "出席"
        elif now < LimitTime[3]:
            status = "遅刻"
        elif now < LimitTime[1]:
            status = "欠席"
        else:
            status = "欠席"

        print(status)

        eel.showIDinfo(stdID[no], stdName[no])
        eel.showNo(no + 1, stdlenx)
        eel.showStatus(status)

        f = open(IOcsvName, "r", encoding="utf-8")
        csv_data = csv.reader(f)
        list = [ e for e in csv_data]
        f.close()

        now = str(now)
        now = now[0:8]
        
        # 更新後のデータ
        data = [stdID[no], stdName[no], stdIDm[no], now, status]

        for i in range(len(list)):
            if list[i][0]==data[0]:
                list[i] = data

        # csv更新
        with open(IOcsvName, "w", encoding="utf_8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(list)

    # タッチのトリガー
    eel.sleep(3)
    for s in range(len(stdIDm)):
        if s != (len(stdIDm)-1):
            if timespan[s]<=0:
                timespan[s] = (timespan[s] * -1) + 1
            print(timespan[s], end=" ")
            print(stdIDm[s])
            touchIDcard(s, stdlen, LimitTime)
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
            touchIDcard(s, stdlen, LimitTime)


@eel.expose
def generateIOcsvName(clid):
    global tcName
    global dcwd
    global IOcwd
    ktcwd = dcwd + "/教員・担当科目リスト.csv"
    crcwd = dcwd + "/講義科目ルール.csv"
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

    IOcsvName = IOcwd + cName + "/" + cName + datew + "出欠リスト.csv"
    print(IOcsvName)
    eel.getcName(cName)
    eel.getIOcsvName(IOcsvName)

@eel.expose
def updateIOcsv(cDataPockets):
    global dcwd
    crcwd = dcwd + "/講義科目ルール.csv"

    newcData = cDataPockets
    print(newcData[0])
    print(newcData[1])
    print(newcData[2])
    print(newcData[3])
    print(newcData[4])

    cName = newcData[0]
    newcDay = newcData[1]
    newcPeri = newcData[2]
    newLT1 = newcData[3]
    newLT2 = newcData[4]

    f = open(crcwd, "r", encoding="utf-8")
    csv_data = csv.reader(f)
    list = [ e for e in csv_data]
    f.close()

    # print(list)

    # newcID
    for s in range(len(list)):
        if list[s][1]==cName:
            basecID = list[s][0]
            tID = list[s][2]
            tName = list[s][3]
            exam = list[s][8]
            sNo = list[s][9]
    newcID = newcDay + newcPeri
    if basecID[-1:] == "1":
        newcID = newcID + "1"
    if basecID[-1:] == "2":
        newcID = newcID + "2"
    if basecID[-1:] == "3":
        newcID = newcID + "3"
    if basecID[-1:] == "4":
        newcID = newcID + "4"

    # cID重複回避
    for t in range(len(list)):
        if list[t][0]==newcID:
            if list[t][1]!=cName:
                excID = list[t][0]
                if excID[-1:] == "_":
                    newcID = newcID + "1"
                elif excID[-1:] == "1":
                    newcID = newcID[:-1] + "2"
                elif excID[-1:] == "2":
                    newcID = newcID[:-1] + "1"
                    if excID[-1:] == "2":
                        newcID = newcID[:-1] + "3"
                elif excID[-1:] == "3":
                    newcID = newcID[:-1] + "4"

    # newCT1, newCT2 (授業開始、終了時刻)
    if newcPeri == "1_":
        newCT1 = "09:00"
        newCT2 = "10:30"
    if newcPeri == "2_":
        newCT1 = "10:40"
        newCT2 = "12:10"
    if newcPeri == "3_":
        newCT1 = "13:00"
        newCT2 = "14:30"
    if newcPeri == "4_":
        newCT1 = "14:40"
        newCT2 = "16:10"
    if newcPeri == "5_":
        newCT1 = "16:20"
        newCT2 = "17:50"
    if newcPeri == "12_":
        newCT1 = "09:00"
        newCT2 = "12:10"
    if newcPeri == "23_":
        newCT1 = "10:40"
        newCT2 = "14:30"
    if newcPeri == "34_":
        newCT1 = "13:00"
        newCT2 = "16:10"
    if newcPeri == "45_":
        newCT1 = "14:40"
        newCT2 = "17:50"

    # newLT1 (出席限度)
    newCT1t = dt.strptime(newCT1, '%H:%M')
    newCT2t = dt.strptime(newCT2, '%H:%M')

    newLT1t = dt.strptime(newLT1, '%H:%M')
    newLT2t = dt.strptime(newLT2, '%H:%M')

    if newLT1t<newCT1t:
        eel.showErrorInfo()
        return
    if newLT2t<newCT1t:
        eel.showErrorInfo()
        return
    if newLT2t<newLT1t:
        eel.showErrorInfo()
        return
    if newCT2t<newLT2t:
        eel.showErrorInfo()
        return

    newLT1t = newLT1t - newCT1t
    newLT2t = newLT2t - newCT1t

    newLT1 = str(newLT1t)
    newLT2 = str(newLT2t)

    print(newLT1)
    print(newLT2)

    newLT1 = newLT1[2:4]
    newLT2 = newLT2[2:4]

    if newLT1 == " d":
        newLT1 = "00"
    if newLT2 == " d":
        newLT2 = "00"
    
    # 更新後のデータ
    data = [newcID, cName, tID, tName, newCT1, newCT2, newLT1, newLT2, exam, sNo]
    print(data)

    for i in range(len(list)):
        if list[i][1]==cName:
            list[i] = data

    # csv更新
    with open(crcwd, "w", encoding="utf_8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list)

    eel.toAdmin()

#出欠リスト表示用
@eel.expose
def chooseIOList(cName, iNo):
    global IOcwd
    path = IOcwd + "/" + cName + "/"
    try:
        IOcsvNames = os.listdir(path)
    except(FileNotFoundError):
        eel.showNameError()
        return
    
    csvNo = len(IOcsvNames)
    listS = []
    sStatusVal = []
    
    for c in range(csvNo):
        IOcsvNamepath = path + IOcsvNames[c]
        print(IOcsvNamepath)
        f = open(IOcsvNamepath, "r", encoding="utf-8")
        csv_data = csv.reader(f)
        listS = [ o for o in csv_data]
        f.close()
        # print(listS)
        sStatusVal.append(listS)

    # 最新の出欠リスト
    IOcsvNamepath = path + IOcsvNames[int(iNo)]
    nIOcsvName = IOcsvNames[int(iNo)]
    
    print(IOcsvNamepath)

    f = open(IOcsvNamepath, "r", encoding="utf-8")
    csv_data = csv.reader(f)
    list = [ e for e in csv_data]
    f.close()

    sID = []
    sName = []
    sIDm = []
    sIntime = []
    sStatus = []
    sStatusValApnd = 0
    sStatusValLate = 0
    sStatusValAbsc = 0
    sStatusRates = []
    sNo = len(list)-1

    for i in range(sNo):
        sID.append(list[i+1][0])
        sName.append(list[i+1][1])
        sIDm.append(list[i+1][2])
        sIntime.append(list[i+1][3])
        sStatus.append(list[i+1][4])

        for x in range(csvNo):
            if sStatusVal[x][i+1][4] == "出席":
                sStatusValApnd += 1
            elif sStatusVal[x][i+1][4] == "遅刻":
                sStatusValLate += 1
            elif sStatusVal[x][i+1][4] == "欠席":
                sStatusValAbsc += 1
        rate = str(sStatusValApnd) + "/" + str(sStatusValApnd + sStatusValLate + sStatusValAbsc)
        # rate = round(rate)
        # rate = str(rate) + "%"
        sStatusRates.append(rate)
        sStatusValApnd = 0
        sStatusValLate = 0
        sStatusValAbsc = 0
    # print(sStatusRates)

    # print(list)

    eel.createIOTable(sID, sName, sIDm, sIntime, sStatus, sStatusRates, sNo, nIOcsvName, csvNo, IOcsvNames)

@eel.expose
def createOneClassGraph(cName, iNo):
    global IOcwd
    # 講義回グラフ作成
    # main author: kurita

    path = IOcwd + "/" + cName + "/"
    IOcsvNames = os.listdir(path)
    print(path)
    print(IOcsvNames)

    # 最新の出欠リスト
    IOcsvName = path + IOcsvNames[int(iNo)]

    #グラフタイトル用の読み込みです。
    file_path = IOcsvName
    file_name_path=os.path.basename(file_path)

    #出席,遅刻,欠席のカウント
    count0 = {}
    with open(IOcsvName,encoding='UTF8') as fo:
        atl_reader = csv.reader(fo)
        atl_header = next(atl_reader)
        # data=fo
        print(atl_header)
        for row in atl_reader:
            data0=row[4]
            count0.setdefault(data0,0)
            count0[data0] +=1

    with open(IOcsvName,encoding='UTF8') as fc:
        line_count=sum([1 for line in fc])

    li_ct=line_count-1
    print(li_ct)
    y_list=[]
    x_label=[]
    #グラフ保存用
    fig=plt.figure()

    plt.title(file_name_path)
    for key0, value0 in count0.items():
        att_counter='{}: {:d}'.format(key0,value0)
        #y軸設定用
        y_list.append(int(value0))
        #x軸の文字ラベル用
        x_label.append('{}'.format(key0))

    #ここでy軸を降順にソート
    y_list2=sorted(y_list,reverse=True)

    #'遅刻''欠席'が一人もいないとき用の処理(y軸用)
    if len(y_list2)==2:
        y_list2.append(0)
        #要素が2つのとき
    elif len(y_list2)==1:
        y_list2.append(0)
        y_list2.append(0)
        #要素が1つのとき
    else:
        y_list2
        #要素が3つのとき

    x=[0,1,2]

    #このex_labelで出席遅刻欠席の順番を指定
    ex_label=['出席','遅刻','欠席']

    #'遅刻''欠席'が一人もいないとき用の処理(x軸用)
    if len(x_label)==2:
        if '出席' in x_label:
            if '遅刻' in x_label:
                x_label.append('欠席')
                #'欠席'がないとき
            else:
                x_label.append('遅刻')
                #'遅刻'がないとき
        else:
            x_label.append('出席')
            #'出席'がないとき　←この場合はいらないとは思うが例外から外すために記載
        #要素が2つのとき    
    elif len(x_label)==1:
        if '出席' in x_label:
            x_label.append('遅刻')
            x_label.append('欠席')
            #'遅刻','欠席'がないとき
        elif '遅刻' in x_label:
            x_label.append('出席')
            x_label.append('欠席')
            #'出席''欠席'がないとき
        else:
            x_label.append('出席')
            x_label.append('遅刻')
            #'出席''遅刻'がないとき ←この場合はいらないとは思うが例外から外すために記載2
    else:
        x_label

    x_label2=sorted(x_label,key=ex_label.index)

    #↓棒グラフ作成
    print(y_list2)
    print(x_label2)
    plt.ylim(0,li_ct)
    graph=plt.bar(x,y_list2)
    #棒の上に数値を挿入するための処理
    height=y_list2
    for rect in graph:
        height=rect.get_height()
        plt.annotate('{}'.format(height),xy=(rect.get_x() + rect.get_width()/2,height),xytext=(0,3),textcoords="offset points",ha='center',va='bottom')

    plt.xticks(x,x_label2)
    plt.show()
    #ここまでが一つの出席リストをグラフ化するスクリプト

@eel.expose
def createCumulativeClassGraph(cName):
    global IOcwd
    # 累積講義グラフ作成
    # main author: kurita

    path = IOcwd + "/" + cName + "/"
    csv_list3 = os.listdir(path)
    os.chdir(path)

    
    #csv_list3=glob.glob("/*.csv")
    #csv_list3
    #print(IOcsvNames)
    print(csv_list3)
    count1 = {}
    # csv_list3=glob.glob(IOcsvNames)
    
    for n in range(len(csv_list3)):
        print(csv_list3[n])
        
        with open(csv_list3[n],encoding='UTF8') as f3:
            atl_reader3 = csv.reader(f3)
            atl_header3 = next(atl_reader3)
            #print(atl_header3)
            for row in atl_reader3:
                data=row[0]
                data2=row[4]
                count1.setdefault(data,0)
                if '出席' in data2:
                    count1[data] +=1
        
        #alatd_list=[]
        
        #各生徒ごとに'出席'の数をカウント
        stnumb_list=[]
        atd_count_list=[]
        

        for key, value in count1.items():
            att_counter='{}: {:d}'.format(key,value)
            #学番と出席数リスト
            #alatd_list.append(att_counter)
            #学番リスト
            stnumb_list.append('{}'.format(key))
            #出席数リスト
            atd_count_list.append(int(value))
        #print(stnumb_list)
        #print(atd_count_list)

    count2 = {}
    for m in range(len(csv_list3)):
        
        with open(csv_list3[m],encoding='UTF8') as f4:
            atl_reader4 = csv.reader(f4)
            atl_header4 = next(atl_reader4)
            #print(atl_header3)
            for row in atl_reader4:
                data3=row[0]
                data4=row[4]
                count2.setdefault(data3,0)
                if '遅刻' in data4:
                    count2[data3] +=1
        
        #alatd_list=[]
        
        stnumb_list2=[]
        atd_count_list2=[]

        for key2, value2 in count2.items():
            att_counter2='{}: {:d}'.format(key2,value2)
            #学番と出席数リスト
            #alatd_list.append(att_counter)
            #学番リスト
            stnumb_list2.append('{}'.format(key2))
            #出席数リスト
            atd_count_list2.append(int(value2))
        #print(stnumb_list)
        #print(atd_count_list)
    
    count3 = {}
    for l in range(len(csv_list3)):
        
        with open(csv_list3[l],encoding='UTF8') as f5:
            atl_reader5 = csv.reader(f5)
            atl_header5 = next(atl_reader5)
            #print(atl_header3)
            for row in atl_reader5:
                data5=row[0]
                data6=row[4]
                count3.setdefault(data5,0)
                if '欠席' in data6:
                    count3[data5] +=1
        
        #alatd_list=[]
        stnumb_list3=[]
        atd_count_list3=[]
        

        for key3, value3 in count3.items():
            att_counter3='{}: {:d}'.format(key3,value3)
            #学番と出席数リスト
            #alatd_list.append(att_counter)
            #学番リスト
            stnumb_list3.append('{}'.format(key3))
            #出席数リスト
            atd_count_list3.append(int(value3))
        #print(stnumb_list)
        #print(atd_count_list)
    #人数
    list_length=len(stnumb_list)
    print(list_length)

    #リストの先頭('出席'と出席数)を削除
    #stnumb_list.remove('出席')

    #atd_count_list.remove(list_length)


    #print(alatd_list)
    #print(stnumb_list)
    #print(atd_count_list)
    #print(stnumb_list2)
    #print(atd_count_list2)

    #↓ここから棒グラフ作成
    fig=plt.figure()
    #学生の数,0から連続した整数のリスト
    y_set=list(range(list_length))

    graph1=plt.bar(y_set,atd_count_list,align="edge",width=-0.5,color="#44cca3",label="出席")
    graph2=plt.bar(y_set,atd_count_list2,align="center",width=0.5,color="#c3cc44",label="遅刻")
    graph3=plt.bar(y_set,atd_count_list3,align="edge",width=0.5,color="#cc5844",label="欠席")
    plt.xticks(y_set,stnumb_list,rotation=90)
    plt.legend()
    plt.show()

    print(os.getcwd())
    os.chdir("./MainProject/")

# # from server import attendlist_send
# from server import gakusei_ex
# from server import gakusei_im
# # from server import exporter
# # from server import get
# # from server import importer
# # from server import kougi_rule_ex
# # from server import kougi_rule_im
# from server import risyuuF1_ex
# from server import risyuuF1_im
# from server import risyuuF2_ex
# from server import risyuuF2_im
# from server import risyuuF3_ex
# from server import risyuuF3_im
# from server import risyuuF4_1_ex
# from server import risyuuF4_1_im
# from server import risyuuF4_2_ex
# from server import risyuuF4_2_im
# from server import risyuuM1_ex
# from server import risyuuM1_im
# from server import risyuuM2_ex
# from server import risyuuM2_im
# from server import risyuuM3_ex
# from server import risyuuM3_im
# from server import risyuuM4_ex
# from server import risyuuM4_im
# from server import risyuuTh2_ex
# from server import risyuuTh2_im
# from server import risyuuTh5_1_ex
# from server import risyuuTh5_1_im
# from server import risyuuTh5_2_ex
# from server import risyuuTh5_2_im
# from server import risyuuTh34_ex
# from server import risyuuTh34_im
# from server import risyuuTu3_1_ex
# from server import risyuuTu3_1_im
# from server import risyuuTu3_2_ex
# from server import risyuuTu3_2_im
# from server import risyuuTu4_ex
# from server import risyuuTu4_im
# from server import risyuuTu5_ex
# from server import risyuuTu5_im
# from server import risyuuW3_1_ex
# from server import risyuuW3_1_im
# from server import risyuuW3_2_ex
# from server import risyuuW3_2_im
# from server import risyuuW4_ex
# from server import risyuuW4_im
# from server import risyuuW5_1_ex
# from server import risyuuW5_1_im
# from server import risyuuW5_2_ex
# from server import risyuuW5_2_im
# from server import risyuuW12_ex
# from server import risyuuW12_im
# from server import tanntou_kyouinn_ex
# from server import tanntou_kyouinn_im
from server import app

@eel.expose
def syncData():
    app.fsync()
#     gakusei_ex.fsync()
#     risyuuF1_ex.fsync()
#     risyuuF2_ex.fsync()
#     risyuuF3_ex.fsync()
#     risyuuF4_1_ex.fsync()
#     risyuuF4_2_ex.fsync()
#     risyuuM1_ex.fsync()
#     risyuuM2_ex.fsync()
#     risyuuM3_ex.fsync()
#     risyuuM4_ex.fsync()
#     risyuuTh2_ex.fsync()
#     risyuuTh5_1_ex.fsync()
#     risyuuTh5_2_ex.fsync()
#     risyuuTh34_ex.fsync()
#     risyuuTu3_1_ex.fsync()
#     risyuuTu3_2_ex.fsync()
#     risyuuTu4_ex.fsync()
#     risyuuTu5_ex.fsync()
#     risyuuW3_1_ex.fsync()
#     risyuuW3_2_ex.fsync()
#     risyuuW4_ex.fsync()
#     risyuuW5_1_ex.fsync()
#     risyuuW5_2_ex.fsync()
#     risyuuW12_ex.fsync()
#     tanntou_kyouinn_ex.fsync()


#     gakusei_im.fsync()
#     risyuuF1_im.fsync()
#     risyuuF2_im.fsync()
#     risyuuF3_im.fsync()
#     risyuuF4_1_im.fsync()
#     risyuuF4_2_im.fsync()
#     risyuuM1_im.fsync()
#     risyuuM2_im.fsync()
#     risyuuM3_im.fsync()
#     risyuuM4_im.fsync()
#     risyuuTh2_im.fsync()
#     risyuuTh5_1_im.fsync()
#     risyuuTh5_2_im.fsync()
#     risyuuTh34_im.fsync()
#     risyuuTu3_1_im.fsync()
#     risyuuTu3_2_im.fsync()
#     risyuuTu4_im.fsync()
#     risyuuTu5_im.fsync()
#     risyuuW3_1_im.fsync()
#     risyuuW3_2_im.fsync()
#     risyuuW4_im.fsync()
#     risyuuW5_1_im.fsync()
#     risyuuW5_2_im.fsync()
#     risyuuW12_im.fsync()
#     tanntou_kyouinn_im.fsync()


#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

