# 큰 수의 법칙
n,m,k=map(int,input().split())
n_list=list(map(int,input().split()))

n_list.sort() # 오름차순으로 정렬
first = n_list[n-1] # 첫번째로 큰 수
second = n_list[n-2] # 두번째로 큰 수
answer=0

# while True:
#     for i in range(k): # 가장 큰 수를 k번 더하기
#         if m==0:
#             break # m이 0이면 반복문 탈출
#         answer += first
#         m-=1 # 가장 큰 수 더할 때마다 m은 하나씩 감소
#     if m==0: # m이 0이면 반복문 탈출
#         break
#     answer += second # 두번째로 큰 수를 한번 더하기
#     m-=1 # 더할 때마다 m은 하나씩 감소
#
# print(answer)

# 더 효율적인 코드 => 반복되는 수열 고려
count = int(m/(k+1))*k + (m%(k+1)) # 가장 큰 수가 더해지는 횟수
answer += count*first #가장 큰 수 더하기
answer += (m-count)*second #두번째로 큰 수 더하기

print(answer)