# 볼링공 고르기

#볼링공 n개, 각 볼링공마다 무게, 공의 번호는 1번부터 순서대로 부여, 같ㅌ은 무게의 공이 있어도 다를ㄴ 공으로 간주, 볼링공 무게 1~m으로 존재, 두 사람이 볼링공을 고르는 경우의 수를 구해라

# 1. 볼링공, 최대 무게, 각 볼링공 무게 입력받기
# 2. result=[]
# 3. for i in n개:
#     for j in i+1~n개:
#         if i의 k!=j의 k:
#             result.append(i,j)
# print(len(result))

#내 풀이
n,m=map(int,input().split())
k=list(map(int,input().split()))

result=0
for i in range(n):
    for j in range(i+1,n):
        if k[i]!=k[j]:
            result+=1
print(result)


# 답지
# a가 특정한 무게를 골랐을때, b가 볼링공을 선택하는 경우를 계산

n,m=map(int,input().split())
k=list(map(int,input().split()))

#1부터 10까지 무게를 담을 수 있는 리스트
array=[0]*11
for x in k:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[x]+=1
result=0
# 1부터 m까지의 각 무게에 대해 처리
for i in range(1,m+1):
    n-=array[i] #무게가 i인 볼링공의 개수(a가 선택할 수 있는 개수)제외
    result+=array[i]*n #b가 선택하는 경우의 수와 곱하기
print(result)