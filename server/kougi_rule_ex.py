# -*- coding: utf-8 -*-

import csv
import MySQLdb

connection = MySQLdb.connect(host="localhost",db="team6",user="root",passwd="",charset="utf8")
cursor=connection.cursor()

cursor.execute("DELETE FROM kougi_rule")

#path変更忘れずに
f = open(".\\MainProject\\data\\講義科目ルール.csv", "r", encoding="utf-8")

reader = csv.reader(f)
header = next(reader)
for row in reader:
  sql = "INSERT IGNORE INTO kougi_rule values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  cursor.execute(sql, (row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
  #print(row)
f.close()


connection.commit()

cursor.close()
connection.close()