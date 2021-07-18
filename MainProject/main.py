### Team6 main.py ###

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
import matplotlib.pyplot as plt
import glob

# import importer
# import exporter

# P000の初期PWは000b

eel.init("MainProject/view")
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

#出欠リストCSV操作
@eel.expose
def openIOcsv(cID, cName):
    global date
    global IOcsvName

    tcxCT1 = {}
    tcxCT2 = {}
    tcxLT1 = {}
    tcxLT2 = {}

    with open("./data/講義科目ルール.csv", "r", encoding="utf_8", errors="", newline="") as p:
        reader = csv.DictReader(p)
        for row in reader:
            tcxCT1[row["科目名"]] = row["開始時間"]
            tcxCT2[row["科目名"]] = row["終了時間"]
            tcxLT1[row["科目名"]] = row["出席限度(分)"]
            tcxLT2[row["科目名"]] = row["遅刻限度(分)"]
    tccCT1 = str(tcxCT1[cName]) + ":00"
    tccCT2 = str(tcxCT2[cName]) + ":00"
    tccLT1 = str(tcxCT1[cName][0:3]) + str(int(tcxCT1[cName][3:5]) + int(tcxLT1[cName])) + ":00"
    tccLT2 = str(tcxCT1[cName][0:3]) + str(int(tcxCT1[cName][3:5]) + int(tcxLT2[cName])) + ":00"
    print(tccCT1)
    print(tccCT2)
    print(tccLT1)
    print(tccLT2)


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

        f = open(IOcsvName, "r", encoding="utf-8")
        csv_data = csv.reader(f)
        list = [ e for e in csv_data]
        f.close()
        
        # 更新後のデータ
        data = [stdID[no], stdName[no], stdIDm[no], now, "出席"]

        for i in range(len(list)):
            if list[i][0]==data[0]:
                list[i] = data

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

def createOneClassGraph(cName):
    # 講義回グラフ作成
    # author: kurita

    IOcsvName = "./Mainproject/IOList/" + cName + "/" + cName + date + "出欠リスト.csv"

    #グラフタイトル用の読み込みです。
    file_path = IOcsvName
    file_name_path=os.path.basename(file_path)

    #出席,遅刻,欠席のカウント
    count = {}
    with open("sample_listbox/保健体育2021-07-07出欠リスト.csv",encoding='UTF8') as fo:
        atl_reader = csv.reader(fo)
        atl_header = next(atl_reader)
        data=fo
        print(atl_header)
        for row in atl_reader:
            data2=row[4]
            count.setdefault(data2,0)
            count[data2] +=1

    with open("sample_listbox/保健体育2021-07-07出欠リスト.csv",encoding='UTF8') as fc:
        line_count=sum([1 for line in fc])

    li_ct=line_count-1
    print(li_ct)
    y_list=[]
    x_label=[]
    #グラフ保存用
    fig=plt.figure()

    plt.title(file_name_path)
    for key, value in count.items():
        att_counter='{}: {:d}'.format(key,value)
        #y軸設定用
        y_list.append(int(value))
        #x軸の文字ラベル用
        x_label.append('{}'.format(key))

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

def createCumulativeClassGraph(cName):
    # 累積講義グラフ作成
    # author: kurita

    IOcsvName = "./Mainproject/IOList/" + cName + "/" + cName + date + "出欠リスト.csv"

    #各生徒ごとに'出席'の数をカウント
    csv_list3=glob.glob(IOcsvName)
    count = {}
    for atdlist_csvdata in csv_list3:
        
        with open(atdlist_csvdata,encoding='UTF8') as f3:
            atl_reader3 = csv.reader(f3)
            atl_header3 = next(atl_reader3)
            #print(atl_header3)
            for row in atl_reader3:
                data=row[0]
                data2=row[4]
                count.setdefault(data,0)
                if '出席' in data2:
                    count[data] +=1
        
        #alatd_list=[]
        stnumb_list=[]
        atd_count_list=[]
        

        for key, value in count.items():
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
    for atdlist_csvdata in csv_list3:
        
        with open(atdlist_csvdata,encoding='UTF8') as f4:
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
    for atdlist_csvdata in csv_list3:
        
        with open(atdlist_csvdata,encoding='UTF8') as f5:
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

    graph1=plt.bar(y_set,atd_count_list,align="edge",width=-0.5,color="green",label="出席")
    graph2=plt.bar(y_set,atd_count_list2,align="center",width=0.5,color="blue",label="遅刻")
    graph3=plt.bar(y_set,atd_count_list3,align="edge",width=0.5,color="red",label="欠席")
    plt.xticks(y_set,stnumb_list,rotation=90)
    plt.legend()
    plt.show()

#これがないと動かないんでよ
while True:
    eel.sleep(2.0)

