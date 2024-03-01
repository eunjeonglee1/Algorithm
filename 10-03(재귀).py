## 함수
def addNumber(num):
    if num ==1:
        return 1
    return num+ addNumber(num-1)

## 메인
print(addNumber(10))


def countDown(n):
    if n == 0:
        print('발사!!')
    else:
        print(n)
        countDown(n-1)

countDown(5)

def printStar(n):
    if n>0:
        printStar(n-1)
        print('*'*n)

printStar(5)

def gugu(dan,num):
    print('%d')