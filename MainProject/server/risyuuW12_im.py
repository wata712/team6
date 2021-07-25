
import pymysql.cursors
import csv


def fsync():
    db=pymysql.connect(host="localhost", user="root", password="" , cursorclass=pymysql.cursors.DictCursor)
    cursor=db.cursor()
    cursor.execute("USE team6")
    sql=('SELECT * FROM w12')
    cursor.execute(sql)
    rows=cursor.fetchall()
    cursor.close()
    db.close()

    if rows:
        columnNames = list()
        # ヘッダデータを作る
        for i in cursor.description:
            columnNames.append(i[0])
        #path変更忘れずに
        with open('.\\MainProject\\data\\履修者-W12_.csv','w',newline='', encoding='utf-8') as csvfile:
            # 辞書順序を指定しておく
            csvwriter = csv.DictWriter(csvfile,columnNames,delimiter=",",quotechar='"')
            # ヘッダ行を書き込み
            csvwriter.writeheader()
            for row in rows:
                #  csv データを書き込み
                csvwriter.writerow(row)
