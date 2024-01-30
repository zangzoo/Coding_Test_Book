# 모험가 길드

n=int(input()) #모험가 수
data=list(map(int,input().split())) #각 모험가들의 공포도 값 리스트

result=0 #모험가의 수
count=0 #현재 그룹에 포함된 모험가의 수

for i in data:
    count+=1
    if count>=i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result+=1 #총 그룹의 수 증가시키기
        count=0 #현재 그룹에 포함된 모험가의 수 초기화

print(result)
