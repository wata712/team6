import MySQLdb
import json

conn = MySQLdb.connect(user='root',
                       password='',
                       host='127.0.0.1',
                       db='team6')
query = "SELECT * FROM gakusei;"
with conn.cursor(MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute(query)
    data = cursor.fetchall()
print(json.dumps(data, indent=4))