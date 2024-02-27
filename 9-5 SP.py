# 전보

# n개의 도시, 통로개수m, 메시지 보내고자하는 도시 c
# 통로에 대한 정보=> 특정도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며 메시지 전달시간은 z이다

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m,c = map(int,input().split())
#각 노드에 연결되어있는 노드에 대한 정보
graph=[[] for _ in range(n+1)]
for i in range(m):
    x,y,z= map(int,input().split())
    graph[x].append((y,z)) #x에서 y로 전달되는 시간 z

distance=[INF]*(n+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #우선순위 큐 사용 => q에 시작비용, 시작노드 집어넣기
    distance[start]=0 #자기자신으로의 거리=0
    while q: #큐가 빌때까지 반복
        dist,now=heapq.heappop(q) # q에서 최단 거리, 그때의 노드 추출
        if distance[now]<dist: #만약에 해당 노드 거리가 추출된 거리보다 작으면 무시
            continue
        for i in graph[now]: #해당 노드와 연결된 (노드,비용) 탐색
            cost=dist+i[1] #비용은 우선순위 큐에서 추출된 최단거리에서 도착 노드까지의 거리를 더한 것
            if cost<distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]]=cost # 최단거리테이블 업뎃
                heapq.heappush(q,(cost,i[0])) #비용,노드 힙에 집어넣기

dijkstra(c)

#도달할 수 있는 노드의 개수
count=0
#도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance=0
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)

# 시작 노드는 제외해야 하므로 count-1을 출력
print(count-1,max_distance)


