import eel

@eel.expose
def sort(text):
    answer = sorted([float(num) for num in text.split(",")])
    eel.showAnswers(answer)

eel.init("view")
eel.start("samplemain.html")
