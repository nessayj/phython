# 튜플 : 변경할 수 없는 시퀀스 자료형이며 ()괄호를 사용하여 생성; 괄호를 안해줘도 상관없음
# 패킹과 언패킹 개념이 있음
# 튜플 정의 하기
person = "연주", 100, "서울" 
print(person)

# 튜플 언패킹 하기(구조분해와 유사)
name, age, city = person # person에 나눠담김
print(name)
print(age)
print(city)


# 튜플을 이용한 함수 반환값 다루기
def get_person() :
    name = "연주"
    age = 100
    city = "서울"
    return name, age, city

result = get_person() # 반환값을 받으면서 바로 패킹
print(result)

# 기본적인 동작
tp = 1,2,3,4,5,6,7,8,9,10
print(tp.count(3)) # 원하는 데이터의 개수를 세어주는 함수(리스트와 동일)
print(tp.index(1)) # 원하는 데이터의 시작 인덱스를 알려 줌
print(len(tp)) # 튜플에 포함된 데이터의 개수
print(tp.__len__())


