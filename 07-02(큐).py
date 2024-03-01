## 함수

# 순차 큐
def isQueueFull():
    global SIZE, queue, front, rear
    # case 1 : 뒤에 여유있음 (가장 쉬운 케이스)
    if (rear!= SIZE-1):
        return False
    # case 2 : 진짜 꽉참
    elif (rear==SIZE-1 and front==-1):
        return True
    # case 3 : 뒤는 마지막, 앞에 여유있음
    elif(rear==SIZE-1 and front!=-1):  # else로 사용가능
        for i in range(front+1, SIZE, 1 ):
            queue[i-1]=queue[i]
            queue[i]=None
        front-=1
        rear-=1
        return False
    # case 3를 else로 사용했을때에
    # else:
    #     for i in range(front + 1, SIZE, 1):
    #         queue[i - 1] = queue[i]
    #         queue[i] = None
    #     front -= 1
    #     rear -= 1
    #     return False



def enQueue(data):
    global SIZE,queue,front,rear
    if (isQueueFull()):
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front==rear):
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅~')
        return
    front+=1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        return
    return queue[front+1]

## 변수

SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=-1

## 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--',queue,'<--입구')

enQueue('재남')
print('출구<--',queue,'<--입구')

retData =deQueue()
print('손님 이리로 : ',retData)

print('준비하세요==>',peek())

retData =deQueue()
print('손님 이리로 : ',retData)

print('준비하세요==>',peek())

retData =deQueue()
print('손님 이리로 : ',retData)

enQueue('재남')
print('출구<--',queue,'<--입구')