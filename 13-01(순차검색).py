## 함수
from random import randint,choice
def seqSearch(ary,fdata):
    pos=-1
    for i in range(0,len(ary)):
        if (ary[i]==fdata):
            pos=i
            break
    return pos
## 변수
dataAry=[randint(30,190) for _ in range(8)] #가족
finddata=choice(dataAry) #누나키


## 메인
print('배열 -->',dataAry)
position=seqSearch(dataAry,finddata)
if (position!=-1):
    print(finddata,'는',position,'위치에 있어요')
else:
    print(finddata, '는', position, '없어요')