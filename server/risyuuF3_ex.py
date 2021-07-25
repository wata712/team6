# -*- coding: utf-8 -*-

import csv
import MySQLdb


def fsync():
  connection = MySQLdb.connect(host="localhost",db="team6",user="root",passwd="",charset="utf8")
  cursor=connection.cursor()

  cursor.execute("DELETE FROM f3")

  #ここでは教員・担当科目リスト.csvをMySQLにinsert
  #path変更忘れずに
  f = open("C:\\Users\\tkr\\Desktop\\team6\\data\\履修者-F3_.csv", "r", encoding="utf-8")

  reader = csv.reader(f)
  header = next(reader)
  for row in reader:
    sql = "INSERT IGNORE INTO f3 values(%s,%s,%s,%s,%s)"
    cursor.execute(sql, (row[0], row[1], row[2],row[3],row[4]))
  f.close()

  connection.commit()

  cursor.close()
  connection.close()