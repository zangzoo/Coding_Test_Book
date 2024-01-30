#문자열 뒤집기

# #내 풀이
# from collections import Counter
# s=input()
# num=[int(s[0])] #첫번째 문자열 num에 집어넣기 => num은 같은 문자인지, 중복을 없애고 비교하기위한 리스트
# count=0
# for i in range(1,len(s)):
#     if num[-1]!=int(s[i]):
#         num.append(int(s[i]))
# num_counts = Counter(num)
# num_min = min(num_counts,key=num_counts.get)
# for j in num:
#     if j==num_min:
#         num_min=max(num)
#         count+=1
#     if len(num)==1:
#         break
# print(count)

#답지
data=input()
count0=0 #전부 0으로 바꾸는 경우
count1=0 #전부 1로 바꾸는 경우

#첫번째 원소에 대해 처리
if data[0]=='1':
    count0+=1
else:
    count1+=1

#두번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1): #data[i+1]을 해주기 위해!!!
    if data[i]!=data[i+1]:
        #다음 수에서 1로 바뀌는 경우:
        if data[i+1]=='1':
            count0+=1
        #다음 수에서 0으로 바뀌는 경우:
        else:
            count1+=1
print(min(count1,count0))
