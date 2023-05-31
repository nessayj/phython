# 객체 소속이 아니고 클래스 소속 메소드 - 정적메소드; 컴파일 시점에 메모리 생성

class Person :
    count = 0
    def __init__(self) : 
        Person.count += 1

    @classmethod
    def print_count(cls) : # cls로 클래스 속성을 접근
        print(f"{cls.count}이 생성 되었습니다.")

james = Person()
maria = Person()
연주 = Person()

Person.print_count()