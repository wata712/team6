
import pymysql.cursors
import csv

db=pymysql.connect(host="localhost", user="watanabe", password="team6pass" , cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
cursor.execute("USE team6")
sql=('SELECT * FROM gakusei')
cursor.execute(sql)
rows=cursor.fetchall()
cursor.close()
db.close()

#もしテーブルが存在しない場合は作成
cursor.execute("CREATE TABLE IF NOT EXISTS scale(Scale TEXT, Root TEXT, I TEXT, IIm TEXT, IIIm TEXT, IV TEXT, V TEXT, VIm TEXT, VIIm TEXT)")

if rows:
    columnNames = list()
    # ヘッダデータを作る
    for i in cursor.description:
        columnNames.append(i[0])
    #path変更忘れずに
    with open('C:\\Users\\tkr\\Desktop\\team6\\server\\test.csv','w',newline='', encoding='utf-8') as csvfile:
        # 辞書順序を指定しておく
        csvwriter = csv.DictWriter(csvfile,columnNames,delimiter=",",quotechar='"')
        # ヘッダ行を書き込み
        csvwriter.writeheader()
        for row in rows:
            #  csv データを書き込み
            csvwriter.writerow(row)
