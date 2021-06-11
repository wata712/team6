import eel
from datetime import datetime as dt

eel.init("view") #HTMLのフォルダ
eel.start("main.html",block=False) #スタートページのファイル名

@eel.expose
def hello():
   print("Hello World!")

#@eel.expose
#def send(msg):
    #print("Received Message: " + msg)
    #return "ok"

@eel.expose
def send(tID,tPW):
   #tID = eel.readtID()()
   print("tID: {}".format(tID))
   #tPW = eel.readtPW()()
   print("tPW: {}".format(tPW))
   return "ok"

while True:
   tID = eel.readtData(0)()
   print("tID: {}".format(tID))
   tPW = eel.readtData(1)()
   print("tPW: {}".format(tPW))
   eel.sleep(2.0)

'''
while True:
   timestamp = dt.now()
   eel.addText("The time now is {}".format(timestamp.strftime("%I:%M:%S %p")))

   eel.sleep(1.0)
'''