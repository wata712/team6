import eel
from datetime import datetime as dt

@eel.expose
def hello():
   print("Hello World!")

@eel.expose
def sort(text):
   answer = sorted([float(num)for num in text.split(",")])
   eel.showAnswers(answer)
   
eel.init("view") #HTMLのフォルダ
eel.start("main.html",block=False) #スタートページのファイル名

while True:
   timestamp = dt.now()
   eel.addText("The time now is {}".format(timestamp.strftime("%I:%M:%S %p")))

   eel.sleep(1.0)