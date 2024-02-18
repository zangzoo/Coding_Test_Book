#미로 탈출

# n*m입력
# 미로 정보 입력
# 괴물 있는 곳 0, 없는 곳 1 => 괴물 피해 탈출 => 탈출하기 위해 움직여야하는 최소 칸의 개수

# n,m=map(int,input().split())
#
# graph=[]
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# result=0
#
# def bfs(x,y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#     if graph[x][y]==1:
#         graph[x][y]=0
#         global result
#         result+=1
#         bfs(x-1,y)
#         bfs(x+1,y)
#         bfs(x,y-1)
#         bfs(x,y+1)
#         return True
#     return False
# for i in range(n):
#     for j in range(m):
#         bfs(i,j)
#
# print(result)
from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 방향 정의 (상하좌우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs구현
def bfs(x,y):
    #큐 구현을 위해 deque라이브러리 사용
    queue=deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        x,y=queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))
