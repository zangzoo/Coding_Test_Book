# 위에서 아래로
n=int(input())

array=[]
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for j in array:
    print(j, end=' ')