import csv

data = []

with open("成績サンプル-UTF8.csv","r",encoding="utf-8") as file:
  reader = csv.reader(file)

  header = next(reader)
  for row in reader:
    data.append(row)

print(len(data))

print(data[0][1])

for i in range(len(data)):
  sum += 1

print(sum)
