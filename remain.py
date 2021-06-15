import eel
import csv
from datetime import datetime as dt

eel.init("view") #HTMLのフォルダ
eel.start("main.html",block=False, port=8010) #スタートページのファイル名

@eel.expose
def hello():
   print("Hello World!")