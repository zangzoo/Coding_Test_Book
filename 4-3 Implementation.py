# 왕실의 나이트 문제

#현재 나이트의 위치 입력받기
input_data=input()
row = int(input_data[1]) #행은 입력값의 인덱스[1]
column = int(ord(input_data[0])-int(ord('a'))) +1 #ord: 문자열을 숫자로 바꿔줌! a를 빼고 1을 더해서 a부터 1이 될 수 있도록!

#나이트가 이동할 수 있는 방향 정의
steps = [(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

#위의 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result=0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row=row+step[0]
    next_col=column+step[1]
    #해당 위치로 이동이 가능하면 result 1 증가
    if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
        result+=1
print(result)