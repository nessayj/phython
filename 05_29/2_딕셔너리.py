# 키와 값이 존재하는 자료 구조(자바의 Map과 유사); {}로 만듬
# 키와 값의 구분은 :콜론으로 구분

coffee_menu = {"Americano" : 2500, "Espresso" : 2500, "Latte": 4000}
tea_menu = {"Black tea" : 4000, "Green tea" : 4000, "Milk tea" : 3500}
food_menu = {"Cake" : 5000, "Bakery" : 6000, "Icecream" : 7000}

print(coffee_menu)

# 키 값으로 값을 확인하기
print(coffee_menu["Americano"])

# get 함수로 값 확인하기
print(coffee_menu.get("Americano"))

# 값 추가, 삭제, 키 존재 여부 확인
# 새로운 키와 값을 추가 : 딕셔너리[키] = 값
# 삭제 : del 딕셔너리[키]
# 키 존재 여부 : if 키 in 딕셔너리
# 딕셔너리의 데이터를 한꺼번에 변경할때 사용 : update함수
# key() : 딕셔너리에서 키를 가져옴
# values() : 딕셔너리에서 값을 가져옴
# items() : 키와 값을 다 가져옴

dict1 = {"자바" : 80, "리액트" : 90, "파이선" : 100}
print(dict1.keys()) # 키값만 가져옴
print(dict1.values()) # value값 만 가져옴
print(dict1.items()) # 키와 값을 다 가져옴
print("리액트" in dict1) # 키 존재 여부 확인; true 값 false값 반환
# print(dict1["자바스크립트"]) # 없는 키를 넣으면 키에러가 발생

# 반복문과 함께 사용
for key in coffee_menu : # 딕셔너리를 키값 기준으로 자동순회
    print(key, ":", coffee_menu[key]) # 조건문을 그냥 넘기고싶으면 pass라고 적어주면됨


# 예제
menu_dic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."] 
}

while True : 
    print("메뉴를 선택하세요 : ")
    menu = input("[1] 메뉴보기, [2] 메뉴 조회, [3] 추가 하기, [4] 삭제 하기, [5] 종료 하기 :" )
    if menu == "1":
        for key in menu_dic : 
            print(key, ":", menu_dic[key])
    if menu == "2":
        rtrv_name = input("조회 할 메뉴를 입력 하세요 : ")
        if rtrv_name in menu_dic : 
            print(menu_dic[rtrv_name])
        else : 
            print("찾는 메ㅈ뉴가 없습니다.")
    if menu == "3" :
        add_name = input("추가 할 메뉴를 입력하세요 : ")
        if add_name not in menu_dic:
            grp = input("카테고리 입력 : ")
            price = int(input("가격 입력 : "))
            desc = input("제품 설명 : ")
            menu_dic[add_name] = [grp, price, desc] # 새로운 키로 값을 추가하기
        else : 
            print("이미 메뉴가 존재합니다.")
    if menu == "4" :
        del_menu = input("삭제 할 메뉴를 입력하세요 : ")
        if del_menu in menu_dic :
            del menu_dic[del_menu]
        else :
            print("삭제 할 메뉴가 없습니다.")
    if menu == "5":
        print("영업을 종료합니다.")
        break
    else : 
        print("잘 못 입력하셨습니다.")


