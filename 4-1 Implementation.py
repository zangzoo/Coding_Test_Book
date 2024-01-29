# 상하좌우 문제
n=int(input()) #크기 입력받기
x,y=1,1 # 처음 위치
plans= input().split() #이동 계획 방향

#L,R,U,D에 따른 이동 방향
dx=[0,0,-1,1] #x값의 변화 -> 상하 이동만 표시 (상단으로 이동 = -1, 하단으로 이동 = 1)
dy=[-1,1,0,0] #y값의 변화 -> 좌우 이동만 표시 (좌로 이동 = -1, 우로 이동 = 1)
move_types=['L','R','U','D']

#이동계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    #공간을 넘어가면 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    #이동 수행
    x,y=nx,ny

print(x,y)