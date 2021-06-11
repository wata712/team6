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
   print("tID: {}".format(tID))
   print("tPW: {}".format(tPW))
   return "ok"

while True:
   tData = eel.readtData()()
   print("tID: {}".format(tData[0]))
   print("tPW: {}".format(tData[1]))
   eel.sleep(2.0)

'''
while True:
   timestamp = dt.now()
   eel.addText("The time now is {}".format(timestamp.strftime("%I:%M:%S %p")))

   eel.sleep(1.0)
'''