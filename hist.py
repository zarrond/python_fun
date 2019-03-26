import matplotlib.pyplot as plt
import numpy as np

data = {}
def read():
    with open('img.txt','r') as f:
        for line in f.readlines():
            line = line[1:7]
            if(line in data):
                data[line] += 1
            else:
                data[line] = 1
read()
#print(data)
dictlist = []
for key, value in data.items():
    temp = [key,value]
    dictlist.append(temp)

numlist = []
for i in dictlist:
    temp = [int(i[0],16),i[1]]
    numlist.append(temp)
    
def myFunc(e):
    return e[0]
 
numlist.sort(key=myFunc)


nums = []
vals = []
for i in numlist:
    nums.append(i[0])
    vals.append(i[1])
print(nums.__sizeof__())
plt.hist([nums,vals],bins = 100)
plt.ylabel('No of times')
plt.show()
