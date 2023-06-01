# 화면을 이용하기 위해 Flask사용; 진입하기 전에 함수로 만들어줘야함
from flask import Flask

app = Flask(__name__) # __name__ 은 현재 모듈 이름을 의미
@app.route("/")
def hello() : 
    return "안녕, 플라스크야"

