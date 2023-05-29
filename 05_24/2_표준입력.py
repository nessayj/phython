# 표준입력 input() :  사용자의 입력을 받아 그 값을 프로그램에서 사용하고자 할 때 사용
# 입력 받은 데이터는 문자열로 반환되며, 원한느 데이터형으로 전달 받기 위해서는 형변환 사용


"""
print("이름을 입력 하세요 : ", end="")
name = input()
print(f"당신의 이름은 {name}입니다")
"""

# name = input("이름을 입력하세요 : ")
# age = int(input("나이를 입력하세요: ")) # 이렇게 하면 형변환을 따로 할 필요없이 int 타입으로 받아짐
# addr = input("주소를 입력하세요 : ")
# score = float(input("성적을 입력 하세요 : "))
# print(f"안녕하세요. {name}님")
# print(f"당신의 주소는 {name}이고, 나이는 {age}, 성적은 {score}입니다.")

# 여러개의 데이터를 한번에 입력받기
# split() : 입력받은 문자열을 공백 기준으로 분리하여 변수에 넣어줌
# map() : 리스트 요소를 지정된 함수로 처리하는 함수

# str1, str2 = input("이름과 주소 입력 : ").split()
# print(f"첫번째 문자열 : {str1},  두번쨰 문자열 : {str2}")


# kor, eng, mat = map(int, input("국어 영어 수학 : ").split())
# print(kor, eng, mat)

"""
score = list(map(int, input("과목제한 없음: ").split()))
print(score)
"""

# 시간을 입력받아 이쁘게 출력
hour, min, sec = map(int, input("시:분:초 입력 ").split(":"))
if hour > 12 : 
    hour -= 12
    print(f"오후 {hour:02}시{min:02}분{sec:02}초")
else :
    print(f"오전 {hour:02}시{min:02}분{sec:02}초")