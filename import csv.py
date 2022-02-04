import csv
f = open('seoul.csv','r',encoding ='cp949')
data = csv.reader(f,delimiter =',')
for row in data:
    print(row)
f.close()
