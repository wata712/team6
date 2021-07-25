from typing import Counter
from warnings import resetwarnings
from bottle import route, run, request, template
import os
import csv


def fsync():
    #http://localhost:5000/login
    #上のリンクに飛ぶ

    #ユーザ情報の読み込み
    user_file = open('server\\security\\user.csv','r')
    user_reader = csv.reader(user_file)
    user_line = [row for row in user_reader]

    #パスワード情報の読み込み
    pass_file = open('server\\security\\pass.csv','r')
    pass_reader = csv.reader(pass_file)
    pass_line = [row for row in pass_reader]

    @route("/login")
    def login():
        return """
        <h1>ログイン</h1>

        <p>ユーザIDとパスワードを入力してください。</p>
        <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
        </form>
        """

    @route("/login", method="POST")
    def do_login():
        username = [request.forms.get("username")]
        for i in range(3):
            #rangeの()内はユーザの人数を入れる
            if username == user_line[i]:
                return do_login_pass(i)
            else:
                None
        return "<p>no such username.</p>"

    def do_login_pass(count):
        password = [request.forms.get("password")]

        if check_login_pass(password,count):
            return index()
        else:
            return """
            <p>Login failed.</p>
            <button type=“button” onclick="location.href='/login'">戻る</button>
            """
<<<<<<< HEAD
    def check_login_pass(password,count):

    if password == pass_line[count]:
        return True
    else:
       return False

#認証後のサイト
@route("/")
def index():
    return """
        <h1><a href="/">管理モード</a></h1>

        <p>開きたいファイルを選択してください</p>

        <!-- ファイル選択画面 -->
        <ul id="menu">
        <li><button type=“button” onclick="location.href='/gakusei_ex'">学生リスト送信</button></li>
        <li><button type=“button” onclick="location.href='/gakusei_im'">学生リストダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/kougi_rule_ex'">講義科目ルール送信</button></li>
        <li><button type=“button” onclick="location.href='/kougi_rule_im'">講義科目ルールダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF1_ex'">履修者-F1送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF1_im'">履修者-F1ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF2_ex'">履修者-F2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF2_im'">履修者-F2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF3_ex'">履修者-F3送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF3_im'">履修者-F3ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF4_1_ex'">履修者-F4_1送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF4_1_im'">履修者-F4_1ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF4_2_ex'">履修者-F4_2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuF4_2_im'">履修者-F4_2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM1_ex'">履修者-M1送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM1_im'">履修者-M1ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM2_ex'">履修者-M2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM2_im'">履修者-M2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM3_ex'">履修者-M3送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM3_im'">履修者-M3ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM4_ex'">履修者-M4送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuM4_im'">履修者-M4ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh2_ex'">履修者-Th2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh2_im'">履修者-Th2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh34_ex'">履修者-Th34送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh34_im'">履修者-Th34ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh5_1_ex'">履修者-Th5_1送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh5_1_im'">履修者-Th5_1ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh5_2_ex'">履修者-Th5_2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTh5_2_im'">履修者-Th5_2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu2_ex'">履修者-Tu2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu2_im'">履修者-Tu2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu3_1_ex'">履修者-Tu3_1送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu3_1_im'">履修者-Tu3_1ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu3_2_ex'">履修者-Tu3_2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu3_2_im'">履修者-Tu3_2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu4_ex'">履修者-Tu4送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu4_im'">履修者-Tu4ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu5_ex'">履修者-Tu5送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuTu5_im'">履修者-Tu5ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW12_ex'">履修者-W12送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW12_im'">履修者-W12ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW3_1_ex'">履修者-W3_1送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW3_1_im'">履修者-W3_1ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW3_2_ex'">履修者-W3_2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW3_2_im'">履修者-W3_2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW4_ex'">履修者-W4送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW4_im'">履修者-W4ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW5_1_ex'">履修者-W5_1送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW5_1_im'">履修者-W5_1ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW5_2_ex'">履修者-W5_2送信</button></li>
        <li><button type=“button” onclick="location.href='/risyuuW5_2_im'">履修者-W5_2ダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/tanntou_kyouinn_ex'">教員・担当科目リスト送信</button></li>
        <li><button type=“button” onclick="location.href='/tanntou_kyouinn_im'">教員・担当科目リストダウンロード</button></li>
        <li><button type=“button” onclick="location.href='/attendlist_ex'">出席者リスト送信</button></li>
        <li><button type=“button” onclick="location.href='/attendlist_im'">出席者リストダウンロード</button></li>
        </ul>

        <button type=“button” onclick="location.href='/login'">ログアウト</button>
        """
=======
>>>>>>> 94d99302c4162580440f02be44677fb27a1c6e81

@route("/gakusei_ex")
def gakusei_ex():
    import gakusei_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/gakusei_im")
def gakusei_im():
    import gakusei_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/kougi_rule_ex")
def kougi_rule_ex():
    import kougi_rule_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/kougi_rule_im")
def kougi_rule_im():
    import kougi_rule_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF1_ex")
def irisyuuF1_ex():
    import risyuuF1_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF1_im")
def risyuuF1_im():
    import risyuuF1_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF2_ex")
def risyuuF2_ex():
    import risyuuF2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF2_im")
def risyuuF2_im():
    import risyuuF2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF3_ex")
def risyuuF3_ex():
    import risyuuF3_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF3_im")
def risyuuF3_im():
    import risyuuF3_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF4_1_ex")
def risyuuF4_1_ex():
    import risyuuF4_1_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF4_1_im")
def risyuuF4_1_im():
    import risyuuF4_1_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF4_2_ex")
def risyuuF4_2_ex():
    import risyuuF4_2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuF4_2_im")
def risyuuF4_2_im():
    import risyuuF4_2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM1_ex")
def risyuuM1_ex():
    import risyuuM1_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM1_im")
def risyuuM1_im():
    import risyuuM1_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM2_ex")
def risyuuM2_ex():
    import risyuuM2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM2_im")
def risyuuM2_im():
    import risyuuM2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM3_ex")
def risyuuM3_ex():
    import risyuuM3_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM3_im")
def risyuuM3_im():
    import risyuuM3_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM4_ex")
def risyuuM4_ex():
    import risyuuM4_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuM4_im")
def risyuuM4_im():
    import risyuuM4_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh2_ex")
def risyuuTh2_ex():
    import risyuuTh2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh2_im")
def risyuuTh2_im():
    import risyuuTh2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh34_ex")
def risyuuTh34_ex():
    import risyuuTh34_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh34_im")
def risyuuTh34_im():
    import risyuuTh34_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh5_1_ex")
def risyuuTh5_1_ex():
    import risyuuTh5_1_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh5_1_im")
def risyuuTh5_1_im():
    import risyuuTh5_1_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh5_2_ex")
def risyuuTh5_2_ex():
    import risyuuTh5_2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTh5_2_im")
def risyuuTh5_2_im():
    import risyuuTh5_2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu2_ex")
def risyuuTu2_ex():
    import risyuuTu2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu2_im")
def risyuuTu2_im():
    import risyuuTu2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu3_1_ex")
def risyuuTu3_1_ex():
    import risyuuTu3_1_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu3_1_im")
def risyuuTu3_1_im():
    import risyuuTu3_1_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu3_2_ex")
def risyuuTu3_2_ex():
    import risyuuTu3_2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu3_2_im")
def risyuuTu3_2_im():
    import risyuuTu3_2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu4_ex")
def risyuuTu4_ex():
    import risyuuTu4_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu4_im")
def risyuuTu4_im():
    import risyuuTu4_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu5_ex")
def risyuuTu5_ex():
    import risyuuTu5_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuTu5_im")
def risyuuTu5_im():
    import risyuuTu5_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW12_ex")
def risyuuW12_ex():
    import risyuuW12_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW12_im")
def risyuuW12_im():
    import risyuuW12_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW3_1_ex")
def risyuuW3_1_ex():
    import risyuuW3_1_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW3_1_im")
def risyuuW3_1_im():
    import risyuuW3_1_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW3_2_ex")
def risyuuW3_2_ex():
    import risyuuW3_2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW3_2_im")
def risyuuW3_2_im():
    import risyuuW3_2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW4_ex")
def risyuuW4_ex():
    import risyuuW4_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW4_im")
def risyuuW4_im():
    import risyuuW4_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW5_1_ex")
def risyuuW5_1_ex():
    import risyuuW5_1_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW5_1_im")
def risyuuW5_1_im():
    import risyuuW5_1_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW5_2_ex")
def risyuuW5_2_ex():
    import risyuuW5_2_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/risyuuW5_2_im")
def risyuuW5_2_im():
    import risyuuW5_2_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/tanntou_kyouinn_ex")
def tanntou_kyouinn_ex():
    import tanntou_kyouinn_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/tanntou_kyouinn_im")
def tanntou_kyouinn_im():
    import tanntou_kyouinn_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/attendlist_ex")
def attendlist_ex():
    import attendlist_ex
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

@route("/attendlist_im")
def tattendlist_im():
    import attendlist_im
    return """<button type=“button” onclick="location.href='/'">戻る</button>"""

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
