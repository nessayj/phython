# 함수나 변수 또는 클래스를 모아 놓은 파일

import math
print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))

from math import sin, cos, tan, floor, ceil # 모듈이름을 빼도 됨
print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))

import math as m
print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(2.5))
print(m.ceil(2.5))


import sys # 시스템 관련 정보를 가지고있는 모듈. 주로 매개변수를 받을 때 사용

# 명령줄 인수 출력
print("명령줄 인수 : ", sys.argv)

# 스트립트 실행 경로
print("실행 경로 : ", sys.path[0])

# 프로그램종료
# sys.exit(0)

import os # 표준 라이브러리, 운영체제와 상호작용하기 위한 기능 제공
# 파일 시스템 접근, 환경변수제어, 프로세스 관리 등 다양한 운영체제 관련 작업을 수행

# 현재 작업 디렉토리 가져오기
cwd = os.getcwd()
print("현재 작업 디렉토리 : ", cwd)

# 파일 존재 여부 확인
is_file = os.path.isfile('test.py')

# 시스템 명령어 출력
os.system("dir")
os.system("ls -l")