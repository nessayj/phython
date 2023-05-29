# 산술연산자 : 더하기, 빼기, 곱하기, 나누기, 나머지, 몫
i, j = 10, 3
"""
print("%d + %d = %d"%(i, j, i+j))
print("%d - %d = %d"%(i, j, i-j))
print("%d * %d = %d"%(i, j, i*j))
print("%d / %d = %.2f"%(i, j, i/j))
print(i/j)
print(i // j) # 몫 구하는 연산자
print(i ** j) # 제곱 연산자
"""

# tax_rate = 0.10
# income = int(input("당신의 수입을 입력하세요"))
# print(f"당신이 내야할 세금은 {income*tax_rate} 에요")

"""
month_pay = float(input("당신의 월 실수령액을 입력 : "))
print(f'당신의 연봉은 {month_pay * 12 * 1.15:.2f} 입니다.')
"""

# 관계연산자 : and, or, not; 대부분의 경우 비교연산자와 함계 사용되며, 참과 거짓을 판별
# and : 둘 다 침이면 참
# or : 둘 중 하나만 참이면 참
# not : 현재의 결과를 부정하는 것
x, y, z = 10, 20, 30
rst1 = (x > 0) and (x > y)
rst2 = (x > 0) or (x > y)
rst3 = not((x > 0) or (x > y))

print(rst1, rst2, rst3)

# 나머지 연산자와 다항연산자
# (조건) and 참인경우 or 거짓인 경우

num = int(input("정수값을 입력 : "))
flag = (num%2 == 0) and "짝수" or "홀수"
print(f"입력하신 숫자는 {flag}입니다.")

age = 23
is_adult = (age >= 20) and "성인" or "미성년자"
print(is_adult)
