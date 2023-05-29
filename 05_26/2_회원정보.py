"""
- 이름 입력
- 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
- 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다.
- 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
- 결과는 마지막에 한번에 출력 한다.
"""


# while True : 
#     name = input("이름을 입력하세요 : ")
#     age = input("나이를 입력하세요 : ")
#     if( 1 <= age <= 199)
#     else: 
#         print("다시 입력하세요 : ")
#         continue
#     gender = input("성별을 입력하세요 남성(M 또는 m) 여성(F 또는 f) : ")
#     if(gender == "M" or "m") : 
#         print("남성")
#     elif (gender == "F" or "f") :
#         print("여성")
#     else: 
#         ("성별을 다시 입력하세요 : ") 
#         continue
#     job = input("직업을 입력하세요 [1] 학생, [2] 회사원, [3] 주부, [4] 무직 : ")
#     if(job == 1) : job == "학생"
#     if(job == 2) : job == "회사원"
#     if(job == 3) : job == "주부"
#     if(job == 4) : job == "무직"
#     else: 
#         ("다시 입력하세요 : ")
#         continue
#     print(f"이름 : {name}")
#     print(f"나이 : {age}" )
#     print(f"성별 : {gender}")
#     print(f"직업 :  {job}")




name = input("이름을 입력 하세요 : ")
while True:
        age = input("나이를 입력하세요 : ")
        if age.isdigit() : # 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
            age = int(age)
            if 0 < age < 200 : break
        print("나이를 잘못 입력 하셨습니다. 다시 입력 하세요.")
            
    
while True:
        gender = input("성별을 입력 하세요 : ")
        if gender == 'M' or gender == 'm': break
        elif gender == 'F' or gender == 'f': break
        else: print("성별이 틀렸습니다. 다시 입력 해 주세요.") 
    
while True:
        jobs = input("직업을 입력 하세요 : ")
        if jobs.isdigit() :
            jobs = int(jobs)
            if 0 < jobs < 5 : break
        print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")
    
if gender == 'M' or gender == 'm': 
    	gen_name = "남성"
else: 
    	gen_name = "여성"
    
jobs_name = ("", "학생", "회사원", "주부", "무직") # 튜플 사용
    
print("="*3, "회원정보", "="*3)     
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_name}")
print(f"직업 : {jobs_name[jobs]}")
