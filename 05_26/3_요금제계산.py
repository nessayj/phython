# 요금제 계산
# 영식요금제 : 30초에 10원
# 민식요금제 : 60초에 15원
# 입력은 첫 줄에 통화 횟수를 입력 받고 다음 줄에는 각 통화에 대한 통화시간을 입력 받음
"""
- 3
- 34 56 78
입력 받고 더 산 요금제가 영식이면 y 출력 민식이면 m 출력 후 요금제 출력
"""

# 통화횟수 입력받음
cnt = int(input("통화횟수"))
call_time = list(map(int, input("통화시간 : ").split()))
y_pay = m_pay = 0

for i in range(cnt) :
    y_pay += (call_time[i] // 30) * 10 + 10
    m_pay += (call_time[i] // 60) * 15 + 15

if(y_pay > m_pay) :
    print("M", m_pay)
elif(y_pay < m_pay) :
    print("Y", y_pay)
else:
    print("M,Y", m_pay)