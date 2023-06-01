import requests # http 요청을 보내고 응답을 받는데 사용하는 라이브러리(get, post, put, delete)
from bs4 import BeautifulSoup # HTML 및 XML 파일에서 데이터를 추출하는데 사용
from flask import Flask


# 기본적인 사용법
"""
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
print(soup)
"""


# 날씨정보 가지고오기
"""
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

# HTTP Get 요청
response = requests.get(url).text
# HTML 파싱
soup = BeautifulSoup(response, "html.parser")
print(soup)

for loc in soup.select("location") : # select 태그선택자 -> 위치정보를 골라 낼 수 있음
    print("도시 : ", loc.select_one("city").string)
    print("날씨 : ", loc.select_one("wf").string)
    print("최저기온 : ", loc.select_one("tmn").string)
    print("최고기온 : ", loc.select_one("tmx").string)
    print("-"*25)
"""

# Flask로 화면출력

app = Flask(__name__)
@app.route("/")

def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"
        
    return output



