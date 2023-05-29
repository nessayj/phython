# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력
result = ""
for e in input() :
    if e.islower() :
        result += e.upper()
    else:
        result += e.lower()
print(result)
