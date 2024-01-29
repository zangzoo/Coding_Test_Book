# 숫자 카드 게임
n,m=map(int,input().split())

result=0

# min() 함수 이용
#한 줄씩 입력받아 확인
for i in range(n):
    data=list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #줄 마다 = 행 마다의 가장 작은 수들 중 가장 큰 수 찾기
    result= max(result,min_value)
print(result)

# 이중 반복문 이용
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split())) #해당 행의 열을 입력받기
    #현재 줄에서 가장 작은 수 찾기
    min_value=10001
    for a in data: # 해당 줄에서 반복
        min_value=min(min_value,a)
    #줄 마다 = 행 마다의 가장 작은 수들 중 가장 큰 수 찾기
    result=max(result,min_value)

print(result)