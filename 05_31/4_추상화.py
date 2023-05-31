# 부모 클래스에서 추상 메소드로 선언한 메소드에 대해서는 반드시 상속 받은 자식 클래스에서 해당 기능을 구현 해야 함

from abc import *  # abc 추상화 예악어

class NetwordAdapter(metaclass=ABCMeta) :
    @abstractmethod
    def connect(self) :
        pass #구현부 없음


class FiveG(NetwordAdapter) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} 5G에 연결하였습니다.")

class WiFi(NetwordAdapter) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} Wi-Fi에 연결하였습니다.")

class LTE(NetwordAdapter) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} LTE에 연결하였습니다.")

net = input("연결할 네트워크를 선택하세요 : [1]5G, [2]Wi-Fi, [3]LTE ")
if net == "1" :
    adapter = FiveG("KT")
    adapter.connect()
elif net == "2" :
    adapter = WiFi("SK")
    adapter.connect()
elif net == "3" :
    adapter = LTE("LG U+")
    adapter.connect()
else : print("연결할 네트워크가 없습니다.")