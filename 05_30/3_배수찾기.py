# 배수찾기
# 문제 : 정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램 작성
# 입력 : 첫째 줄에 n이 주어진다. 다음 줄 부터 한줄에 한 개씩 목록에 들어있는 수가 주어진다.
# 이 수는 0 보다 크고, 10,000보다 작다
# 목록은 0으로 끝난다
# 출력 : 목록에 있는 수가 n의 배수인지 아닌지를 구한 뒤 예제 출력 처럼 출력
# -------------------
# 예제입력
# 3
# 1
# 7
# 99
# 321
# 777
# 0
# --------------------
# 예제출력
# 1 is NOT a multiple of 3.
# 7 is NOT a multiple of 3.
# 99 is a multiple of 3.
# 321 is a multiple of 3.
# 777 is a multiple of 3.
"""
정수 n을 입력받음
목록을 저장할 빈 리스트 생성
무한의 반복문을 수행하면서 목록을 입력받고 0 이 되면 빠져나감
입력받은 목록을 순회하면서 목록의 값과 주어진 n값이 배수이지 비교해서 출력
"""

# num = (int, input("나눌 숫자를 입력하세요 : "))
# num_list = list(map(int, input("나눠질 숫자들을 입력하세요 (종료를 원하시면 0을 눌러주세요): ").split()))

# for e in num_list :
#     if(e == 0) : 
#         break
#     elif(e / num == 0) :
#         print(f"{e} is multiple of {num}")
#     else :
#         print(f"{e} is NOT a multiple of {num}")

n = int(input())
ls = []

while True : 
    x = int(input())
    if x == 0 : break
    ls.append(x)

for e in ls :
    if e % n  == 0 : print(f"{e} is a multiple of {n}")
    else : print(f"{e} is NOT a multiple of {n}")