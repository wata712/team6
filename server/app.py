from bottle import route, run, request
import os
 
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
    username = request.forms.get("username")
    password = request.forms.get("password")
    if check_login(username, password):
        return "<p>Your ligin infomation was correct.</p>"
    else:
        return "<p>Login failed.</p>"
 
def check_login(username, password):
    if username == "user" and password == "pass":
        return True
    else:
        return False
 
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))