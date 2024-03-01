## 함수
from random import randint,choice
def binSearch(ary,fdata):
    pos=-1
    start=0
    end=len(ary)-1
    while (start<=end):
        mid = (start+end)//2
        if (ary[mid]==fdata):
            pos=mid
            break
        elif (ary[mid]<fdata):
            start=mid+1
        else:
            end=mid-1
    return pos
## 변수
dataAry=[randint(30,190) for _ in range(10)] #가족
finddata=choice(dataAry) #할머니키
dataAry.sort()


## 메인
print('배열 -->',dataAry)
position=binSearch(dataAry,finddata)
if (position!=-1):
    print(finddata,'는',position,'위치에 있어요')
else:
    print(finddata, '는', position, '없어요')