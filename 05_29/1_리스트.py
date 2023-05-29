# 연속적으로 데이터를 저장하는 자료형, 동적으로 크기가 변경됨.
# 다른타입의 데이터를 함께 사용 가능(다른배열, 다른타입)
# 읽고 쓰기가 가능 []

number = [1,2,3,4,5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "apple", True, 2.31 , [1,2,3,4,5]]

# 데이터타입이 없기 때문에 변수 설정을 잘 해줘야 함
empty = []
str_n = ""

# 변수 사용 대비 이점
# kor, eng, mat = map(int, input("성적입력: ".split())
# tot = kor + eng + mat
# print(f"평균 : {tot/3}")

# 리스트 사용; 값이 들어오면 알아서 배열이 늘어남
# score = list(map(int, input("성적입력").split()))
# print(f"평균 : {sum(score)/len(score)}")

s = ["korea", "seoul", "inchun", [1,2,3,4,5], ["연주","연주다","집에가고싶다"]]
print(s[0][1])
print(s[3][4])
print(s[4][2][0])

# 리스트 연산자 : 연결(+), 반복(*)
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a * 3)
print(list_a + list_b)

# 리스트 요소 추가 : append, insert
# append : 리스트 끝에 값을 추가하는 함수; O(1)
# insert : 특정 위치에 값을 추가하는 함수 ; O(n)
# 삽입, 삭제를 자유롭게하려면 linked list 사용하면됨(자바에서)

list_a.append(4)
list_a.append(5)
list_a.insert(0, 10) # 0번 인덱스에 10을 삽입   
print(list_a)

# 리스트 제거하기
# pop : 인덱스가 없으면 마지막 요소 반환 후 삭제
# 인덱스가 있으면 인덱스 위치의 데이터 삭제, 인덱스 범위를 벗어나면 에러출력
# remove : 값으로 제거, 동일한 값이 여러개 있는 경우 낮은 인덱스 부터 제거
# clear : 모든 값을 삭제하고 빈 리스트만 남김
# del 리스트명[인덱스] : 해당 값 제거

list_all = [0,1,2,3,4,5,6,7,8,9,"a", "b", "c", "d", "e", "f","korea", "seoul", "gangnam"]
list_all.pop() # 인덱스가 없으므로 마지막 요소 제거
list_all.pop(8)
list_all.insert(8, 8)
del list_all[10]

list_all.clear()
print(list_all)

# 중복 제거
my_list = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'F']
new_list= []
for e in my_list: # my_list 리스트를 요소값 기준으로 자동 순회
    if e not in new_list: 
        new_list.append(e) # 리스트의 끝에 값을 추가하는 함수
print(new_list)

# 정렬
arr = [1, 4, 5, 666, 999, 1000, 2, 3, 4, 6]
arr.sort() # 오름차순 정렬
print(arr)
arr.sort(reverse=True) # 내림차순 정렬
print(arr)

# 리스트 모든 요소 스캔(탐색)
# 자바의 향상된 for문과 같이 리스트의 요소를 자동 순회
name_x = ["John", "George", "Paul", "Ringo"]
for e in name_x:  # 요소를 이용하여 탐색
    print(e)

# 리스트의 개수를 구해서 인덱스로 순회
for i in range(len(name_x)): # 인덱스를 이용하여 탐색; 
    print(name_x[i])


# 응용문제 : 홀수, 짝수 나누어담기
# 무작위 수를 공백으로 기준하여 입력받아 홀수와 짝수로 리스트에 나누어 담아 출력
number = list(map(int, input("입력 : ").split()))
even = [] # 짝수를 저장 할 리스트
odd = [] # 홀수를 저장 할 리스트
for e in number :
    if e % 2 == 0:  even.append(e)
    else: odd.append(e)
print(f"홀수 : {odd}")
print(f"짝수 : {even}")


# 람다를 이용한 방법으로 풀기
number = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda x: x % 2 ==1 , number)) # 리액트 구현시; (x) => x % 2 ==1
even = list(filter(lambda x: x % 2 ==0 , number))

print(f"홀수 : {odd}")
print(f"짝수 : {even}")





