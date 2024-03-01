##함수

from random import randint
def findMinindex(ary):
    minIdx=0
    for i in range(1,len(ary),1):
        if (ary[minIdx]>ary[i]):
            minIdx=i
    return minIdx

## 변수

# testAry=[55,88,33,77]
testAry=[randint(0,100) for _ in range(30)]

## 메인

print(testAry)
minPos = findMinindex(testAry)
print('제일 작은 값 : ',testAry[minPos])