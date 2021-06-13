import eel
from datetime import datetime as dt

eel.init("view") #HTMLのフォルダ
eel.start("main.html",block=False) #スタートページのファイル名

@eel.expose
def hello():
   print("Hello World!")

'''
@eel.expose
def send(tID,tPW):
   print("tID: {}".format(tID))
   print("tPW: {}".format(tPW))
   return "ok"
'''

@eel.expose
def registtData(tData):
   tID = tData[0]
   tPW = tData[1]
   print("tID: {}".format(tID))
   print("tPW: {}".format(tPW))
   return 0

'''
while True:
   timestamp = dt.now()
   eel.addText("The time now is {}".format(timestamp.strftime("%I:%M:%S %p")))

   eel.sleep(1.0)
'''