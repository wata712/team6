import pymysql.cursors
import csv
import tkinter as tk

root = tk.Tk()
root.geometry("300x100")
root.title("ファイルの名前入力")

entry = tk.Entry()
entry.place(x=20, y=30)

button = tk.Button(text="OK")
button.place(x=150, y=26)

def click():
    word = entry.get()
    entry.delete(0, tk.END)
    label = tk.Label(text=word)
    label.place(x=20, y=50)

button["command"] = click    #関数と関連付ける

root.mainloop()


#接続する
connect = pymysql.connector.connect(
user='watanabe',
password='team6pass',
host='localhost',
database='team6')

#カーソルを作成
cursor = connect.cursor()

#もしテーブルが存在しない場合は作成
cursor.execute("CREATE TABLE IF NOT EXISTS (Scale TEXT, Root TEXT, I TEXT, IIm TEXT, IIIm TEXT, IV TEXT, V TEXT, VIm TEXT, VIIm TEXT)")
#

with open("scale.csv", "r") as file:
rows = csv.reader(file)
for row in rows:
#最初の行は取り除く
#データの挿入
cursor.execute('INSERT INTO scale (Scale, Root, I, IIm, IIIm, IV, V, VIm, VIIm) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)


#変更を反映させる
connect.commit()

#中身を確認する
# cursor.execute('select * from scale')
# result = cursor.fetchall()
# print(result)

cursor.close()
connect.close()
