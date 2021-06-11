import cgi
import os

# デバッグ用
import cgitb
cgitb.enable()

print ("Content-Type: text/html")
print()

print ("<html><body>")

form = cgi.FieldStorage()
form_check = 0

# formでの変数有無チェック
if "name" not in form or "addr" not in form:
  form_check = 1

print ("<h1>{0}変数出力</h1>".format(os.environ['REQUEST_METHOD']))

# パラメータエラー時の対応 
# python の cgiモジュールは変数取得のためにGET/POSTメソッドによって
# 処理を変更する必要はないのでメチャ楽だ！
if form_check == 1 :
  print ("<h2>ERROR !</h2>")
  print ("Please fill in the name and addr fields.")
else :
  print ("<b>名前: </b>", form["name"].value)
  print ("<b>住所: </b>", form["addr"].value)

print ("</body></html>")