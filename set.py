import eel

eel.init("web")
eel.start("set.html", block=False, port=9999)

while True:
    eel.sleep(2.0)
