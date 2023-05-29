# 작은 따옴표 3개를 사용해도 동일
print("""동해물과 백두산이 마르고 닳도록 하는님이
보우하사 우리나라만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
""")


print("저의 이름은 '연주'입니다")
print("저의 이름은 \"연주\"입니다")

# 이스케이프 문자 사용하기
print("서울시\t강남구 \t역삼동")
print("사과\r 바나나\r 오렌지") # r=> 커서를 맨앞으로 보내서 덮어서 다음 단어가 노출

# 인덱싱(슬라이싱) : 인덱스는 항상 0에서 부터 시작
jumin = "991120-1234567"
print("성별 : " + jumin[7])
print("태어난 연도 : " + jumin[:2]) # 앞에 값을 주지않으면 0번인덱스부터 시작하고 2미만까지
print('월 : ' + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

print("안녕하세요"[0])
print("안녕하세요"[:2])
print("안녕하세요"[-3:])
print("안녕하세요"[7:]) 

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

# a[1] ="K" 문자열 요소는 변경할 수 없음

# 대소문자 바꾸기
a = "Hello Python Program..."
print(a.upper())
print(a.lower())

# 문자열 변경하기 : replace("","")
input_str = "Hello Python Program"
input_str.replace("Python", "React")
new_str = input_str.replace("Python", "React")
print(input_str)
print(new_str)

# 문자열에 포함 된 문자 갯수 세기 및 문자열 길이 
# 갯수세기 : count()
# 길이 반환: __len__(), len()
print(input_str.count("l")) # "l" 문자가 몇번나오는지 갯수세기
print(len(input_str)) # lent() 함수사용; 외부함수를 가지고와서 카운트
print(input_str.__len__()) # 문자열에 포함된 내장함수사용

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 첫 번째 인덱스 반환, 문자열을 찾지 못하면 -1을 반환
# index() : 찾은 문자열의 첫 번째 인덱스 반환, 문자열을 찾지못하면 ValueError라는 예외를 발생시킴
# rfind() : 뒤에서 찾기 시작하지만 인덱스 번호는 앞에서부터 반환

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장")) # 가장 좋은 선물은 용서에서의 가장을 찾음 하지만 인덱스번호는앞에서 세서 34
print(phrase.index("가장"))

# 없는 문자열 찾기
print(phrase.find("나에게")) # 없는 문자열은 -1 반환
# print(phrase.index("나에게")) 찾을 수 없기 때문에 에러

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 연산자
# "문자열" + "문자열"
# "문자열" * 3 : 뒤에 오는 숫자 만큼 문자열을 반복
print("태양고" * 2)
print("안녕", "!"*5, "\n", "\t", "="*3, "\n나희도" * 3, "입니다")
print("안녕", "!"*5, "\n", "\t", "="*3, "\n나희도" * 3, "입니다", sep="")

# 문자열의 양옆의 공백 제거 : strip()
input_a =  """
    안녕하세요.
문자열의공백을 제거합니다
"""
print(input_a.strip())



