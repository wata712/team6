import csv

def stdSim(cID):
    #講義IDに一致した履修者csvを開く
    stdcsvName = "./data/履修者-" + cID + ".csv"
    with open(stdcsvName, "r", encoding="utf_8", errors="", newline="") as p:
        reader = csv.DictReader(p)

    ## codearea ##
    #cID 講義ID
    #IDm IDm
    #StdID 学籍番号
    #StdName 名前
    #inTime 入室時間(講義開始10分前を中心として定数とか使った正規分布で生成して)

    return (IDm, StdID, StdName, inTime)