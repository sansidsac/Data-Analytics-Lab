import csv

def read_file(filename):
    data=[]
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

data=read_file('apriori.csv')

min_support=2
min_confidence=0.7

freq={}

for i in range(1,len(data)):
    for j in range(len(data[i])):
        if (data[i][j]) in freq:
            freq[(data[i][j])]+=1
        else:
            freq[(data[i][j])]=1


for i in range(1,len(data)):
    for j in range(len(data[i])):
        for k in range(j+1,len(data[i])):
            if(data[i][k]<data[i][j]):
                item=(data[i][k],data[i][j])
            else:
                item=(data[i][j],data[i][k])
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1

for i in range(1,len(data)):
    for j in range(len(data[i])):
        for k in range(j+1,len(data[i])):
            for l in range(k+1,len(data[i])):
                if(data[i][k]<data[i][j]):
                    if(data[i][j]<data[i][l]):
                        item=(data[i][k],data[i][j],data[i][l])
                    elif(data[i][l]<data[i][k]):
                        item=(data[i][l],data[i][k],data[i][j])
                elif(data[i][j]<data[i][k]):
                    if(data[i][k]<data[i][l]):
                        item=(data[i][j],data[i][k],data[i][l])
                    elif(data[i][l]<data[i][j]):
                        item=(data[i][l],data[i][j],data[i][k])
                elif(data[i][l]<data[i][k]):
                    item=(data[i][j],data[i][l],data[i][k])
                else:
                    item=(data[i][k],data[i][l],data[i][j])
                if item in freq:
                    freq[item]+=1
                else:
                    freq[item]=1

for x in freq.copy():
    if freq[x]<min_support:
        del freq[x]

print("Frequent Itemsets:")

for x in freq:
    print(x , ":", freq[x])