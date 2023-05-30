# 입력 받은 수가 소수인지 아닌지 판별하기 (함수 이용)
# 소수란? 1과 자기자신 이외에 나누어지지 않는 수

# num = (int, input("숫자를 입력하세요 :"))

# while True :
#     if num / 3 == 0 : 
#         print(f"{num}은 소수가 아닙니다.")
#         break
#     elif num / 2 == 0 :
#         print(f"{num}은 소수가 아닙니다.")
#         break
#     elif num / 5 == 0 :
#         print(f"{num}은 소수가 아닙니다.")
#         break
#     elif num / 7 == 0 :
#         print(f"{num}은 소수가 아닙니다.")
#         break
#     else : 
#         print(f"{num}은 소수가 입니다.")
#         break



def is_prime(n) :
    for i in range(2, n) : # 1과 자기 자신 제외
        if n % i == 0 : return False
    return True

n = int(input("정수 입력 : "))

if (is_prime(n)) : print(f"{n}은 소수 입니다.")
else : print(f"{n}은 소수가 아닙니다.")    