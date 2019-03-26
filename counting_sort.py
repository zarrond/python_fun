#sort 
from array import *
import time
def randArray(n,arr2fill):
    from random import randint
    for i in range(0,n):
        arr2fill.append(randint(0,255))
    return arr2fill

def countingSort(inputArr, key):
    _newArr = array('I')
    _count = array('I')
    for i in range(0,256):
        _count.append(0)
    
    for x in inputArr:
        _count[key(x)] += 1
    _total = 0
    _oldCount = 0
    for i in range(0, len(_count)):
        _oldCount = _count[i]
        _count[i]  = _total
        _total += _oldCount
    for x in inputArr:
        _newArr.append(0)
    for x in inputArr:
        _newArr[_count[key(x)]] = x
        _count[key(x)] += 1;
    return _newArr
    
    
    
def key(x):
    '''Function used to create index from array element'''
    return x
    

arr2sort = array('I')
sortedArr = array('I')
arr2sort = randArray(10000,arr2sort)
print(arr2sort)
timeS = time.time_ns()
sortedArr = countingSort(arr2sort,key)
timeF = time.time_ns()
print(sortedArr)
print("all time {}ms".format((timeF-timeS)/10**6))