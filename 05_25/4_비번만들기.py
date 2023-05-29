"""
규칙1 : http://naver.com에서 앞의 http:// 잘라내기

규칙2 : 처음 만나는 점(.) 이후는 제외 

규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 +글자에 포함된 'n' 갯수+ '!' + 자신의이니셜(예: 'jks')
"""


file_name = "password.txt"
f = open(file_name, "wt") # write 텍스트 모드
while True: 
    url = input("사이트 : ")
    if url == "exit" : break
    my_str = url.replace("http://", "") # 문자를 대체하기떄문에 이렇게 하면 저 문자열이 지워짐
    my_str = my_str[:my_str.index(".")] # 위에서 잘라진 문자열에서 . 위치 미만까지 잘라짐
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("n")) + "!" + "jyj"
    print(password)
    f.write(password + "\n")
f.close();
