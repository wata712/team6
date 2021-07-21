from typing import Counter
from bottle import route, run, request
import os
import csv

#http://localhost:5000/login
#上のリンクに飛ぶ

user_file = open('C:/user.csv','r')
user_reader = csv.reader(user_file)

pass_file = open('C:/pass.csv','r')
pass_reader = csv.reader(pass_file)

user_line = [row for row in user_reader]
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
        if username == user_line[i]:
            return do_login_pass(i)
        else:
            None
    return "<p>no such username.</p>"

def do_login_pass(count):
    password = [request.forms.get("password")]

    if check_login_pass(password,count):
        return "<p>Your ligin infomation was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login_pass(password,count):

    if password == pass_line[count]:
        return True
    else:
       return False

 
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))