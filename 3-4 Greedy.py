# 1이 될 때까지
n,k=map(int,input().split())
cnt=0

# 단순 방법
# n이 k이상이라면 k로 계속 나누기
while n>=k:
    # n이 k로 나누어 떨어지지 않으면 n-1
    while n%k != 0:
        n-=1
        cnt+=1
    # k로 나누기
    n//=k
    cnt+=1

# 마지막으로 남은 수에 대해 1씩 빼기
while n>1:
    n-=1
    cnt+=1
print(cnt)

# 방법2
while True:
    #(n==k로 나누어떨어지는 수)가 될때까지 1씩 빼기
    target = (n//k)*k
    cnt += (n-target)
    n=target
    # n이 k보다 작을 때 = 더이상 나눌 수 없을 때 반복문 탈출
    if n<k:
        break
    #k로 나누기
    cnt+=1
    n//=k
#마지막으로 남은 수에 대해 1씩 뺴기
cnt+=(n-1)
print(cnt)