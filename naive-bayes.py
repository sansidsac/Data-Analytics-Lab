import csv

def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

data=read_file('naive-bayes.csv')
# print(data)
req=[['age','youth'],['income','medium'],['student','yes'],['credit_rating','fair']]

yesno=[[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

pyes=0.0
pno=0.0
yescount=0.0
nocount=0.0

for i in range(1,15):
    if data[i][5]=='yes':
        yescount+=1
    else:
        nocount+=1

pyes=yescount/14

pno=nocount/14

for i in range(4):
    rnum=1
    for k in range(6):
        if req[i][0]==data[0][k]:
            rnum=k
            break
    val=req[i][1]
    pvalyes=0.0
    pvalno=0.0
    for j in range(1,15):
        if data[j][rnum]==val and data[j][5]=='yes':
            pvalyes+=1
        if data[j][rnum]==val and data[j][5]=='no':
            pvalno+=1
    pvalyes/=yescount
    pvalno/=nocount
    yesno[i][0]=pvalyes
    yesno[i][1]=pvalno

theyes=yesno[0][0]*yesno[1][0]*yesno[2][0]*yesno[3][0]*pyes
theno=yesno[0][1]*yesno[1][1]*yesno[2][1]*yesno[3][1]*pno

finalyesno='no'

if theyes>theno:
    finalyesno='yes'

print("Probability Table:")
print("Probability for yes: ",theyes)
print("Probability for no: ",theno)
print("Predicted class_buys_book for [youth,medium,yes,fair]: ",finalyesno)


