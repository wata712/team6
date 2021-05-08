import csv
def takara2(i=1):
  print(data[i])
  

def takara():
  #ハローワールドを出力する
  print("hello world")

data = []

with open("成績サンプル-UTF8.csv","r") as file:
  reader = csv.reader(file)

  header = next(reader)
  for row in reader:
    data.append(row)

#print(data)

#test_potato
print(len(data))



print(data[0][1])
takara()

takara2()