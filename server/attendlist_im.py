# -*- coding: utf-8 -*-

import glob
import csv
import tkinter as tk
import pymysql.cursors


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



db=pymysql.connect(host="localhost", user="watanabe", password="team6pass" , cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
cursor.execute("USE team6")
sql=('SELECT * FROM '+word)
cursor.execute(sql)
rows=cursor.fetchall()
cursor.close()
db.close()

Name = ""
Name2 = ""
files = glob.glob(".\\MainProject\\IOList\\**\\"+ word + ".csv")
for file in files:
  print(file)
  Name = file
  Name2 = Name.replace("\\","\\\\")
  print(Name2)

if rows:
  columnNames = list()
  # ヘッダデータを作る
  for i in cursor.description:
    columnNames.append(i[0])
  #path変更忘れずに
  with open(Name2,'w',newline='', encoding='utf-8') as csvfile:
    # 辞書順序を指定しておく
    csvwriter = csv.DictWriter(csvfile,columnNames,delimiter=",",quotechar='"')
    # ヘッダ行を書き込み
    csvwriter.writeheader()
    for row in rows:
        #  csv データを書き込み
        csvwriter.writerow(row)
