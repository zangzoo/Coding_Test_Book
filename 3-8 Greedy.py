#만들 수 없는 금액

# #오답
# n=int(input())
# money=list(map(int,input().split()))
# money_comb=[]
# max_money=0
# money_sum=[]
# from itertools import combinations
# for i in range(1,n+1):
#     money_comb.append(list(combinations(money,i)))
#     for j in range(1,len(money_comb)+1):
#         max_money += money_comb[j]
#         money_sum.append(max_money)
#         print(money_sum)
# all=[i for i in range(1,max_money+1)]
# print(min(all-money_sum))

#답지
n=int(input())
data=list(map(int,input().split()))
data.sort()

target=1
for x in data:
    #만족할 수 없는 금액을 찾았을 때 반복 종료
    if target<x:
        break
    target+=x
#만들 수 없는 금액 출력
print(target)