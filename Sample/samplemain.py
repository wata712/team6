import eel

@eel.expose
def sort(text):
    answer = sorted([float(num) for num in text.split(",")])
    eel.showAnswers(answer)

eel.init("Sample/view")
eel.start("samplemain.html", port=8080)