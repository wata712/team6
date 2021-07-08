import csv

def stdSim(cID):
    #学籍番号を(ランダムに)生成して
    for i in range(1, 101):
        temNo = "S" + str(i)
        print(temNo)
        #if文とかで"S001" "S012"のように3桁表示になるようにして

    stdIDmx = {} #辞書型
    stdIDm = [] #配列
    #講義IDに一致した履修者csvを開く
    stdcsvName = "./data/履修者-" + cID + ".csv"
    with open(stdcsvName, "r", encoding="utf_8", errors="", newline="") as p:
        reader = csv.DictReader(p)
        for row in reader:
            stdIDmx[row["学籍番号"]] = row["IDm"]
    for i in range(len(row)):
        stdIDm = str(stdIDmx[temNo])
    print(stdIDm)

    #上のかたまり周辺でfor文とか使ってうまいことやって
    #雛形には多分エラーあるからうまいこといじって

    ## memoarea ##
    #cID 講義ID
    #IDm IDm csvママ 1次元配列

    ###！！！ 以下の変数は実装しなくていいです ！！！###
    #inTime 入室時間 1次元配列 個々の形式:str(hh:mm:ss) 例 inTime[0] : 08:43:21 (講義開始10分前を中心として定数とか使った正規分布で生成)
    #StdID 学籍番号 csvママ 1次元配列
    #StdName 名前 csvママ 1次元配列

    return stdIDm

print(stdSim("Tu4_"))