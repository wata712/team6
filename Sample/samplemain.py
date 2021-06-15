import eel

def main():
    eel.init("Sample/view")
    eel.start("samplemain.html", port=8000)


"""link1が押下された際に呼び出すスクリプト"""
@eel.expose
def link1_click():
    print("link1_clicked")

"""link2が押下された際に呼び出すスクリプト"""
@eel.expose
def link2_click(args):
    print(args)
    return "link2_clicked"

if __name__ == '__main__':
     main()