# 조건문 : if ~ else
"""
num = int(input("정수를 입력하세요 : "))
if num % 2 == 0 : 
    print("짝수 입니다.")
else : 
    print("홀수 입니다.")
"""

# 조건문 : if ~ elif ~ else
"""
n = int(input("정수입력 : "))
if n > 100 : 
    print("100보다 커요")
elif n < 100 :
    print("100보다 작아요")
else : 
    print("100과 같아요")
"""

# 문자열 비교 조건문
"""
print("지금 계절은? : ", end='');
season = input()
if season == "spring": print("봄이 왔어요.")
elif season == "summer": print("여름이 왔어요.")
elif season == "fall" or "autumn" : print("쓸쓸한 가을 입니다.")
elif season == "winter": print("아직 겨울이네요ㅠㅠ")
else : pass
"""

"""
age = int(input("나이를 입력하세요: "))
# 파이선에서는 if (0 < age < 100) 로 간단하게 쓸 수 있음
if(age > 0 and age < 100) :
    print("정상입력")
else : 
    print("잘못입력")
"""


# 회원가입을 위한 아이디와 패스워드 입력받기
# string.find(찾을문자)
# string.find(찾을문자, 시작 index)
# string.find(찾을문자, 시작 index, 끝 index)
user = input("아이디를 입력하세요 : ")
if len(user) >=10 : 
    pw = input("비밀번호 입력 : ")
    if pw.__len__() < 8 or pw.__len__() > 16 :
        print("비밀번호는 8자에서 16자사이어야 합니다.")
    else :
        print(f"아이디는 {user}이고 비밀번호는 {pw}입니다.")
else : 
    print("아이디는 반드시 10자리 이상이어야 합니다.")