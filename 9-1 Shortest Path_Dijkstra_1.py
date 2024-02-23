# 간단한 다익스트라 알고리즘

import sys
input= sys.stdin.readline
INF= int(1e9) #무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
# 시작 노드 번호 입력받기
start=int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[]for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited=[False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF #초기값 설정
    index=0 #초기값 설정 => 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1): # 모든 노드들 비교
        if distance[i] < min_value and not visited[i]: #현재의 최솟값보다 i의 거리가 더작고, 방문한 적이 없다면
            min_value = distance[i] #최솟값을 i의 거리로 설정
            index = i #최단거리인 인덱스 i로 설정
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0 #시작노드 거리는 0 (자기 노드-> 자기 노드 니까)
    visited[start] = True # 시작 노드 방문처리
    for j in graph[start]: # 시작 노드의 graph에서 => j = 해당 노드의 (도착, 비용) 리스트 탐색
        distance[j[0]] = j[1] # 시작 노드에서 도착지점까지 거리 = 해당 노드의 비용으로 설정하기 (순차적으로 탐색, 계산됨)
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1): # i가 시작노드를 제외한 나머지 노드들에서 반복
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node() # 현재 = 가장 최단 거리가 짧은 노드
        visited[now]=True # 현재 노드 방문 처리
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: # 현재 노드의 graph에서 => j = 현재 노드의 (도착, 비용) 리스트 탐색
            cost = distance[now] + j[1] # 비용 = 현재노드까지 거리 + 현재노드에서 도착 노드까지의 비용 (순차적으로 탐색, 계산됨)
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range (1,n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력®
    if distance[i]==INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

