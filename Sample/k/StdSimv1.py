import csv
import random

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
            
    print(stdcsvName)
    print(len(stdIDm))
    return stdIDm
    
print("start:")
print(stdSim("W5_1"))

    #上のかたまり周辺でfor文とか使ってうまいことやって
    #雛形には多分エラーあるからうまいこといじって

    ## memoarea ##
    # 返り値はstdIDm(リスト)のみ
    # with open でCSVを開くのは1度だけ(効率が非常に悪いのでfor文の中にwith openを入れないで)

    #cID 講義ID
    #stdIDm 生徒のIDm csvママ 1次元配列

    ###！！！ 以下の変数は実装しなくていいです ！！！###
    #inTime 入室時間 1次元配列 個々の形式:str(hh:mm:ss) 例 inTime[0] : 08:43:21 (講義開始10分前を中心として定数とか使った正規分布で生成)
    #StdID 学籍番号 csvママ 1次元配列
    #StdName 名前 csvママ 1次元配列

