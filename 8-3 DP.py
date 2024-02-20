#개미 전사

n=int(input()) #식량창고 개수
k=list(map(int,input().split())) #각 창고별 저장된 식량 수

#앞서 계산된 결과를 저장하기 위한 dp테이블
d=[0]*100


#다이나믹 프로그래밍(바텀업)
d[0]=k[0]
d[1]=max(k[0],k[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+k[i])

print(d[n-1])
