print(39) # 정수형
print("문자열")
print([1,2,3,4,5]) #리스트형
print(1+2)
print("파" + "이" + "선")
print("파""이""선")
print("파", "이", "선") #콤마는 기본적으로 띄어쓰기가 포함
print("파\n\n이\n\n썬")
print("\"안녕하세요\"라고 말하쥐마~~")


# end와 sep옵션
# end는 한줄 찍고 뭘할거냐
# sep은 구분자 뒤에 어떤역할을줄것이냐
print("Hello", end="\n") #end특성의 기본적인 옵션은 줄바꿈
print("파이선...><")

print("hello", end="@")
print("파이선")

print("hello", end="\t") #문장끝나고 tap만큼떨어져있음
print("파이선")

print(1,2,3,4,5,sep="\t") # 사이가 벌어짐

print("010", "1234", "1234", sep="-")

year = 2023
month = 5
day = 24
print(year, month, day, sep="/")

# 다양한 출력 스타일
# 버전마다 출력스타일이 다르기 때문에 다 알아야함
# c언어 출력스타일도 알아야함

name="연주"
age=100
gender="내가누구냐"
job = "직업,,,휴,,, 하고싶지않아요"
addr = "집도없다"

#C언어 스타일 => %로 서식을 지정
print("="*5, "C스타일", "="*5)
print("이름: %s"%(name))
print("나이: %d"%(age))
print("성별: %s"%(gender))
print("주소: %s"%(job))
print("주소: %s"%(addr))

#파이썬 스타일 : 3.6 이전 버전에서 주로 사용
print("="*5, "파이선올드스타일", "="*5)
print("이름: {}, 주소: {} ".format(name, addr))
print("나이: {}".format(age))

#파이썬 스타일 : 3.6 이후 스타일
print("="*5, "파이선 새로운 스타일", "="*5)
print(f"이름: {name}")
print(f"나이: {age}")
print(f"성별: {gender}")
print(f"직업: {job}")
print(f"주소: {addr}")

#자바스타일
print("="*5, "자바스타일", "="*5)
print("이름: " + name)
print("나이 : " + str(age))
print("성별: " + gender)

#출력 포맷 정렬
# < : 좌측정렬
# > : 우측정렬
# ^ : 중앙정렬
print("|{:5}|".format(10))
print("|{:<5}|".format(10))
print("|{:>5}|".format(10))
print("|{:^5}|".format(10))

# 최신스타일
num = 10
print(f"|{num:5}|")
print(f"|{num:<5}|")
print(f"|{num:>5}|")
print(f"|{num:^5}|")

# 소수점 이하 자르기
print(f"{3.1415922345:.2f}")





