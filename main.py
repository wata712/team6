import eel

@eel.expose
def pythonfunc():
   return "Ello from Python!"
   
eel.init("view") #HTMLのフォルダ
eel.start("main.html") #スタートページのファイル名