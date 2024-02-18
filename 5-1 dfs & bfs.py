#음료수 얼려먹기 문제 => 연결요소 찾기 => 묶음 찾기

#첫줄: 얼음틀의 세로길이 n, 가로길이 m
#둘째줄: 얼음틀의 형태 (뚫려있으면0, 칸막이1)
#출력: 한번에 만들 수 있는 아스크림 개수

n,m=map(int, input().split())

#2차원의 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 방문하지 않았다면
    if graph[x][y]==0:
        #해당 노드 방문처리
        graph[x][y]=1
        #상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

#모든 노드(위치)에 대해 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        #현재위치에서 dfs수행
        if dfs(i,j)==True:
            result+=1
print(result)