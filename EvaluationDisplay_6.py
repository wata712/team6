import csv

def ave():
  sum = 0
  for i in range(len(data)):
    sum += int(data[i][1])
  return sum

def hyoujunn():
  h = 0
  for i in range(len(data)):
    a = float(data[i][1])
    h += (heikinn-a)**2
  ans = h/len(data)
  return ans


data = []

with open("成績サンプル-UTF8.csv","r",encoding="utf-8") as file:
  reader = csv.reader(file)

  header = next(reader)
  for row in reader:
    data.append(row)

sum2 = ave()
heikinn = sum2/len(data)
stde = hyoujunn()

print("平均は" + str(heikinn))
print("標準偏差は"+str(stde))
