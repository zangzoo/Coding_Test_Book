# 시각 문제
h=int(input())

cnt=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 문자열'3'이 포함돼있으면 cnt +1
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print(cnt)