## 함수
def isStackFull():
    global SIZE, stack, top
    if(top==SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE,stack,top
    if(isStackFull()==True):
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅~')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅~')
        return
    return stack[top]

def checkBracket(ex) :
    for ch in ex :
        if ch =='(':
            push(ch)
        elif ch == ')':
            data = pop()
            if (data=='('):
                pass
            else:
                return False
    if top == -1: # 스택이 깔끔하게 비어있는지?
        return True
    else:
        return False


## 변수
SIZE=50   #전역상수. 대문자로 표기
stack=[None for _ in range(SIZE)]
top=-1

## 메인
expr=''
retTF=checkBracket(expr)

print(expr)
if (retTF):
    print('정상')
else:
    print('오류')