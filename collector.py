'''
# 패키지 다운로드 방법
# pip : 파이썬으로 작성된 패키지 소프트웨어를 설치하거나 관리하는 패키지 관리 시스템
# 1. 아래 terminal 탭 클릭 후 -> pip install '원하는 패키지 이름'   (ex. pip install pymysql)
# 2. 설치 된 모듈 리스트 : ctrl + alt + s (file -> setting ->project:bot -> python interpreter)

/* 패키지 설치 */
# pip install <package name>

/* 설치된 패키지 업그레이드 */
# pip install --upgrade <package name>

/* 패키지 제거 */
# pip uninstall <package name>

/* 설치된 패키지 파일 목록 */
# pip list


'''

print("collector 프로그램이 시작 되었습니다!")
# crtl + alt + 좌우방향키 : 이전 커서 위치로

# 아래 세줄 -> mysql이라는 데이터베이스를 사용하기 위해 필요한 패키지들 -> 암기X! 그냥 다음에 mysql을 사용하고 싶으면 아래 세 줄을 복사, 붙여넣기

# mysql 파이썬이랑 연결하기위해서 만들어 놓은거다
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
##########################################

class Collector:
    def __init__(self):
        print("__init__ 함수에 들어왔습니다.")
        self.engine_bot = None  # 인스턴트 변수를 만들어주고 값을 넣어주고

    def db_setting(self, db_name, db_id, db_passwd, db_ip, db_port):
        print("db_setting 함수에 들어왔습니다.")
        # mysql 데이터베이스랑 연동하는 방식.
        self.engine_bot = create_engine("mysql+mysqldb://" + db_id + ":" + db_passwd + "@"
                                        + db_ip + ":" + db_port + "/" + db_name, encoding='utf-8') #mysql 이랑 연동을 해주었음

#  __name__ ? => 현재 모듈의 이름을 담고 있는 내장 변수, 우리는 colector라는 파일을 실행한다! -> 이 파일의 __name__ 내장변수에는 __main__ 이 저장되어있다
# import openapi를 통해서 openapi소스코드를 참고를 하는 경우 openapi 모듈의 __name__은 "openapi" 가 저장 되어 있다.
# openapi 파일을 실행하면 그때는 참고 한 것이 아니기 때문에 __name__에는 __main__ 이 저장 되어 있다.
print("collector.py 의 __name__ 은?: ", __name__)
if __name__ == "__main__":
    print("__main__에 들어왔습니다.")
    # c = collector() 이렇게 c라는 collector라는 클래스의 인스턴스를 만든다.
    # 아래 클래스를 호출하자마다 __init__ 함수가 실행이 된다.
    c = Collector()
    # db_name 이라는 변수에 우리가 조회 하고자 하는 데이터베이스의 이름을 넣는다.
    db_name = 'bot_test1'
    # mysql db 계정
    db_id = 'bot'#root 로 해두된다
    # mysql db ip (자신의 PC에 DB를 구축 했을 경우 별도 수정 필요 없음)
    db_ip = 'localhost'  # localhost : 자신의 컴퓨터를 의미
    # mysql db 패스워드
    db_passwd = 'H1p2k3vudrkd'
    # db port가 3306이 아닌 다른 port를 사용 하시는 분은 아래 변수에 포트에 맞게 수정하셔야 합니다.
    db_port = '3305'

    c.db_setting(db_name, db_id, db_passwd, db_ip, db_port)

    # 데이터베이스에 실행 할 쿼리
    sql = "select * from bot_test1.class1;"

    # 위의 sql 문을 데이터베이스에 실행한 결과를 rows라는 변수에 담는다.
    rows = c.engine_bot.execute(sql).fetchall()  # C라는 객체에서 엔진봇을 가져와 excute sql을해주고 가져와주는거다
    print(rows)
