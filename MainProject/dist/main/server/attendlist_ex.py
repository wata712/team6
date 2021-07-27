# -*- coding: utf-8 -*-

import glob
import mysql.connector
import csv
import tkinter as tk
import MySQLdb
import os


def fsync():
	cwd = os.getcwd()
	IOcwd = cwd + "\\IOList"
	root = tk.Tk()
	root.geometry("300x100")

	entry = tk.Entry()
	entry.place(x=20, y=30)

	button = tk.Button(text="OK")
	button.place(x=150, y=26)

	word = ""

	def click():
			global word
			word = entry.get()
			entry.delete(0, tk.END)
			label = tk.Label(text=word)
			label.place(x=20, y=50)

	button["command"] = click    #関数と関連付ける

	root.mainloop()

	cnx = None

	try:
			cnx = mysql.connector.connect(
					user='root',  # ユーザー名
					password='',  # パスワード
					host='localhost',  # ホスト名(IPアドレス）
					database='team6'  # データベース名
			)

			cursor = cnx.cursor()

			sql = '''
			CREATE TABLE ''' + word + '''(
					学籍番号 VARCHAR(255) NOT NULL,
					氏名 VARCHAR(255) NOT NULL,
					IDm VARCHAR(255) NOT NULL,
					入室時刻 VARCHAR(255) NOT NULL,
					出欠 VARCHAR(255) NOT NULL
			)'''

			cursor.execute(sql)

			cursor.execute("SHOW TABLES")
			print(cursor.fetchall())

			cursor.close()

	except Exception as e:
			print(f"Error Occurred: {e}")

	finally:
			if cnx is not None and cnx.is_connected():
					cnx.close()


	connection = MySQLdb.connect(db="team6",user="root",passwd="",charset="utf8")
	cursor=connection.cursor()

	cursor.execute("DELETE FROM " + word)

	#ここでは教員・担当科目リスト.csvをMySQLにinsert
	#path変更忘れずに
	Name = ""
	Name2 = ""
	files = glob.glob(".\\dist\main\\IOList\\**\\"+ word + ".csv")
	for file in files:
		Name = file
		Name2 = Name.replace("\\","\\\\")

	f = open(Name2, "r", encoding="utf-8")
	reader = csv.reader(f)
	header = next(reader)
	for row in reader:
		sql = "INSERT IGNORE INTO "+word+" values(%s,%s,%s,%s,%s)"
		cursor.execute(sql, (row[0], row[1], row[2],row[3],row[4]))  
	f.close()

	connection.commit()

	cursor.close()
	connection.close()