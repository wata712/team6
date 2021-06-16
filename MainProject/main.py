import eel

eel.init("MainProject/view")
eel.start("main.html", block=False)

@eel.expose
def registtData(tData):
   tID = tData[0]
   tPW = tData[1]
   print("tID: {0} tPW: {1}".format(tID, tPW))

#これがないと動かない
while True:
    eel.sleep(2.0)