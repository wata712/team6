# -*- coding: utf-8 -*-

import csv
import MySQLdb


def fsync():
  connection = MySQLdb.connect(host="localhost",db="team6",user="root",passwd="",charset="utf8")
  cursor=connection.cursor()

  cursor.execute("DELETE FROM tanntou_kyouinn")

  #ここでは教員・担当科目リスト.csvをMySQLにinsert
  #path変更忘れずに
  f = open("C:\\Users\\tkr\\Desktop\\team6\\data\\教員・担当科目リスト.csv", "r", encoding="utf-8")

  reader = csv.reader(f)
  header = next(reader)
  for row in reader:
    sql = "INSERT IGNORE INTO tanntou_kyouinn values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (row[0], row[1], row[2],row[3],row[4],row[5]))
  f.close()

  connection.commit()

  cursor.close()
  connection.close()