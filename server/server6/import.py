# -*- coding: utf-8 -*-

import csv
import MySQLdb

connection = MySQLdb.connect(db="team6",user="root",passwd="")
cursor=connection.cursor()

f = open("教員・担当科目リスト.csv", "r")

reader = csv.reader(f)
header = next(reader)
for row in reader:
  sql = "INSERT IGNORE INTO receive values(%s,%s,%s,%s,%s,%s)"
  cursor.execute(sql, (row[0], row[1], row[2],row[3],row[4],row[5]))
f.close()

connection.commit()

cursor.close()
connection.close()