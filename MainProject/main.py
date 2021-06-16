import eel

eel.init("MainProject/view")
eel.start("main.html", block=False)

@eel.expose
def send(msg):
    print("Received Message: " + msg)
    return "ok"

while True:
    text = eel.readTextBox()()
    print("Text box contents: {}".format(text))
    eel.sleep(2.0)