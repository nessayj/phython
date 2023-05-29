# 내장함수 : 파이선에서 기본적으로 제공하며, import 없이 사용


print(max([1,2,3,4,5,6,7,8,9]))

ls = [10,2,33,41,25,6,7,8,9]
print(sum(ls) / len(ls)) #평균구하기

print(sorted(ls)) # 정렬 : 작은수에서 큰수

# 몫과 나머지 반환
print(divmod(sum(ls), 5)) # 몫과 나머지 결과가 두개 반환(구조분해)

# 외장 함수(import 해서 사용) : random
import random

# 지정한 범위 내의 임의이 수를 구하는 함수
rand = random.randint(0,4) # 0 ~ 4사이의 임의의 값 생성
print(rand)

rand1 = random.randrange(0,4) # 0이상 4미만의 임의의 값 생성
print(rand1)

# 현재 시간 가져오기
from datetime import datetime

date = datetime.today()
year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
hour = datetime.today().hour
minute = datetime.today().minute
second = datetime.today().second


print(date)
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)


# 중복값이 없는 로또번호만들기
print("로또번호 자동생성 : ", end="")
ls = [] # 대괄호로 빈 리스트생성
while True:
    rand = random.randrange(1, 46)
    if rand not in ls: # rand 값이 ls에 포함되어있지않으면 (중복제거)
        ls.append(rand) # append; 추가해라
    if len(ls) == 6: break
print(ls)