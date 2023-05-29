# 입력 받은 n개의 원소에 대한 평균구하기
# split은 공백기준으로 자름; list는 동적으로 크기르 결정해서 인풋받은 갯수만큼 배열을 만들어줌
value = list(map(int, input("정수 입력: ").split())) 
print(sum(value)/len(value))


# 정수 n을 입력받아 n * n 출력
n = int(input("정수입력: "))
for i in range(1, n*n+1): # n은 그 값 미만 값이기 때문에 +1 해줘야함
    print(f"{i:4}", end="") # 4칸공백을 잡고 오른쪽 정렬
    if(i%n == 0) : print() # 배수가 될 때만 줄바꿈


# n개에 대한 숫자를 입력받아 최소값 및 최대값 구하기
n = list(map(int, input().split()))
print(min(n))
print(max(n))


# 주민등록번호를 입력받아 생년월일, 성별, 나이 출력
from datetime import datetime
current_year = datetime.today().year
jumin = input("주민번호를 입력하세요: ")
jumin_year = int(jumin[:2])
jumin_gender = int(jumin[7])
jumin_month = int(jumin[2:4])
jumin_day = int(jumin[4:6])

if jumin_gender == 1 or jumin_gender == 2:
    age = current_year - 1900 - jumin_year
else :
    age = current_year - 2000 - jumin_year
if jumin_gender == 1 or jumin_gender == 3:
    gender = "남성"
else:
    gender = "여성"

print(f"당신은 {jumin_year:02}년 {jumin_month:02}월 {jumin_day:02}일 생입니다.")
print(f"당신의 성별은 {gender}입니다.")
print(f"당신의 나이는 {age}입니다.")


# 알람설정하기
hour, min = map(int, input("시간입력: ").split())
tmp = (hour*60) +min
if tmp < 45:
    tmp = (24 * 60) + min
tmp -= 45
hour = tmp // 60 # 몫에 대한 연산
min = tmp % 60

print(f"{hour} {min}")


