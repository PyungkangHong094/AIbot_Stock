# collector_v3
# 매일 장 마감후에 자동으로 이 프로그램이 계속 돌아가는게 목적이다
# 데이터들을 수집합니다
# 데이터-> 종목 리스트 혹은 종목별 일별 데이터 종가 시가 등등

# TODO List
# 이 수많은 데이터들을 통해서 종목리스트를 어떻게 받아오고 어떻게 테이블이 생겼는지 알아보는게 목표
# version 1.3.2
print("collector 프로그램이 시작 되었습니다!")

from library.collector_api import *

class Collector:
    print("collector 클래스에 들어왔습니다.")

    def __init__(self):
        print("__init__ 함수에 들어왔습니다.")
        self.collector_api = collector_api()

    def collecting(self):
        self.collector_api.code_update_check()

if __name__ == "__main__":
    print("__main__에 들어왔습니다.")
    # 아래는 키움증권 openapi를 사용하기 위해 사용하는 한 줄! 이해 할 필요 X
    app = QApplication(sys.argv)
    c = Collector()
    # 데이터 수집 시작 -> 주식 종목, 종목별 금융 데이터 모두 데이터베이스에 저장.
    c.collecting()
