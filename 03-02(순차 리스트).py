## 함수
def add_data(friend):
    katok.append(None)  # 1단계 : 빈칸 추가
    klen=len(katok)
    katok[klen-1]=friend  # 2단계 추가한 빈칸에 친구 넣기
def insert_data(position,friend):
    katok.append(None)  # 1단계 : 빈칸 추가
    klen=len(katok)
    # 2단계 : 한칸씩 뒤로 이동(마지막 친구~바로 다음)
    for i in range(klen-1,position,-1):  #어려운코드
        katok[i]=katok[i-1]
        katok[i-1]=None   #생략가능
    # 3단계 : 포지션 자리에 친구 넣기
    katok[position]=friend

def delete_data(position):
    # 1단계 : 위치 친구 지우기
    katok[position]=None
    klen=len(katok)
    # 2단계 : 지운 친구 다음부터, 마지막 친구까지 앞으로 이동
    for i in range(position+1,klen,1) :
        katok[i-1] = katok[i]
        katok[i] = None
    # 3단계 마지막칸 제거
    del(katok[klen-1])


## 변수
katok=[]

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)


insert_data(3,'미나')
print(katok)

delete_data(4) # 사나(사나) 카톡 차단
print(katok)