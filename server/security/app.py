from typing import Counter
from bottle import route, run, request, template
import os
import csv

#http://localhost:5000/login
#上のリンクに飛ぶ

#ユーザ情報の読み込み
user_file = open('C:/Users/浅田恒樹/server/user.csv','r')
user_reader = csv.reader(user_file)
user_line = [row for row in user_reader]

#パスワード情報の読み込み
pass_file = open('C:/Users/浅田恒樹/server/pass.csv','r')
pass_reader = csv.reader(pass_file)
pass_line = [row for row in pass_reader]

@route("/login")
def login():
    return """
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

def check_login_pass(password,count):

    if password == pass_line[count]:
        return True
    else:
       return False

#認証後のサイト
@route("/")
def index():
    return template('index')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))