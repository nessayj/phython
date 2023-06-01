# 예외처리 : 실행도중에 발생하는 문제를 처리하기 위해 사용(회피가능한 문제에 대해서 처리)

try :
    print("나눗셈 계산기 입니다")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError :
    print("에러!!!! 값이 잘못되었습니다.")
except ZeroDivisionError as err :
    print(err)
except Exception as err :
    print(err)
else : 
    print("정상처리 되었습니다.")
finally :
    print("프로그램 실행 완료^^*")

# 오류회피
# 해당 파일이 없으면 에러가 발생하지만 이 경우는 그냥 지나 감
try : 
    score_file = open("1score.txt", "r", encoding="utf8")
    print(score_file.read())
    score_file.close()
except FileNotFoundError :
    pass