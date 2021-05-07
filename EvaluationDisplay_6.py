import csv

data = []

with open("成績サンプル-UTF8.csv","r") as file:
  reader = csv.reader(file)

  header = next(reader)
  for row in reader:
    data.append(row)

#print(data)

print(len(data))

print(data[0][1])

for i in range(len(data)):
  sum += data[i][1]

print(data)