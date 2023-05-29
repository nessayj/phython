# 한번에 변수에 값 할당
a = b = c = 1
print(a,b,c)


# 변수를 재 할당 해줘도 됨

a, b, c = 1, True, "곰돌이"
print(a,b,c)

# 변수의 타입확인(타입은 int, boolean, string, float 네개만 존재)
age = 100
is_adult = True
gender = "male"
score = 95.97


print(type(age))
print(type(is_adult))
print(type(gender))
print(type(score))

# 데이터의 형변환 - 선언된 변수에 값이 할당되는 순간에 형이 결정 되고 이 후 다른 데이터형으로 변경하는 것을 의미 함
print(10+int("10"))
print("나이: " + str(33))
print(f"나이 : {33}")

a, b = 10, "20"
print(a+ int(b))
x, y, z, a, b, c = -1, 10, "test", "", None, 0  # 0을 제외한 정수값은 true / 공백과 0, false, None은 false
print(bool(x))
print(bool(y))
print(bool(z))
print(bool(a))
print(bool(b))
print(bool(c))








