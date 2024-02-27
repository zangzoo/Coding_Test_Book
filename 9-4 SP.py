# 미래 도시
# 모든 지점에서 다른 모든 지점까지의 최단거리 구해야함 => 플로이드워셜 문제

INF=int(1e9)

n,m=map(int,input().split())

# 2차원 리스트
graph=[[INF]*(n+1) for i in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 각 간선에 대한 정보 입력받기
for _ in range(m):
    # a 에서 b로 가는 시간은 1
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1 #양방향이니까

# x, k 입력받기
x,k=map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][i]+graph[b][i])

distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print(-1)
else:
    print(distance)

