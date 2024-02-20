#1로 만들기

# x=int(input())
# cnt=0
#
# def make_1(x):
#     global cnt
#     while x >= 1:
#         if x % 5 == 0:
#             cnt += 1
#             x //= 5
#         elif x % 3 == 0:
#             cnt += 1
#             x //= 3
#         elif x % 2 == 0:
#             cnt += 1
#             x //= 2
#         elif x==1:
#             break
#         else:
#             x -= 1
#             cnt += 1
#     return cnt
#
# print(make_1(x))

x=int(input())

#앞서 계산된 결과 담기 위한 dp테이블
d=[0]*30001

#다이나믹 프로그래밍 진행 (보텀업)
for i in range(2,x+1):
    #현재의 수에서 1 빼는 경우
    d[i]=d[i-1]+1
    #현재의 수가 2로 나누어 떨어지는 경우
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    #현재의 수가 3으로 나누어 떨어지는 경우
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    #현재의 수가 5로 나누어 떨어지는 경우
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)

print(d[x])