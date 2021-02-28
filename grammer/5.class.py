print("\n*************************************ex1*************************************")
'''
현재 계좌에 보유한 모든 종목(삼성전자, SK텔레콤)을 출력하라.
'''

# 종목명
stock_name1 = '삼성전자'
# 현재가
price1 = 60900
# 수익률
rate1 = 3.5
print(f"stock_name: {stock_name1}, price: {price1}, rate: {rate1}")

stock_name2 = 'SK텔레콤'
price2 = 238000
rate2 = 20
print(f"stock_name: {stock_name2}, price: {price2}, rate: {rate2}")

# '현대자동차를 매수 하면?'
stock_name3 = '현대자동차'
price3 = 165500
rate3 = 3
print(f"stock_name: {stock_name3}, price: {price3}, rate: {rate3}")



print("\n*************************************ex2*************************************")
''' 
[클래스, 객체]
    ex1을 클래스를 사용해서 표현하면? => 종목단위로 묶어서 간결하게 나타 낼 수 있다. 
    - 클래스(class) : ex) 붕어빵틀, 자동차 설계도 
                     속성(상태)과 기능(동작)으로 구성
    - 객체(object) :  클래스를 바탕으로 찍어낸 제품 ex) 붕어빵, 자동차
'''


#  tab 키로 띄워서
class Stock:  # Stock 이라는 이름을 가진 클래스를 정의
    def __init__(self, stock_name, stock_price, stock_rate):  # __init__: '생성자'(특별한 함수) 라고 한다. 클래스의 객체를 만들 때 자동으로 실행이 된다.
        self.name = stock_name  # 인스턴스변수 : self.name, self.price, self.rate를 인스턴스 변수라고 한다.
        self.price = stock_price
        self.rate = stock_rate


# item1, item2, item3은 객체 (=Stock이라는 클래스의 인스턴스)
# 삼성전자'를 Stock 클래스의 __init__ 생성자의 두번째 매개변수인 stock_name 전달.
# 60900는 stock_price로 전달
# 3.5는 stock_rate로 전달
item1 = Stock('삼성전자', 60900, 3.5)
item2 = Stock('SK텔레콤', 238000, 20)
item3 = Stock('현대자동차', 165500, 3)

print(f"stock_name: {item1.name}, price: {item1.price}, rate: {item1.rate}")
print(f"stock_name: {item2.name}, price: {item2.price}, rate: {item2.rate}")
print(f"stock_name: {item3.name}, price: {item3.price}, rate: {item3.rate}")

# python console에서도 테스트 해보세요!


print("\n*************************************ex3*************************************")
'''

** self ??
    - class 안의 함수들은 첫 매개변수(=parameter) 로 self 를 사용
    - self는 해당 클래스의 객체 자신.  
    - 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한 것
'''


class Stock2:  # Stock2 이라는 이름을 가진 클래스를 정의
    def __init__(self, stock_name, stock_price, stock_rate):  # 메서드(method = function) : 클래스 내부에 정의 된 함수
        self.name = stock_name  # 인스턴스변수 : self.name, self.price, self.rate를 인스턴스 변수라고 한다.
        self.price = stock_price
        self.rate = stock_rate
        print(f" self 의 일련번호: {id(self)}")


# item1, item2, item3은 객체 (=Stock2이라는 클래스의 인스턴스)
item1 = Stock2('삼성전자', 60900, 3.5)

# id() 내장 함수는 객체를 입력값으로 받아서 객체의 고유값(일련번호)을 반환하는 함수
# 출력 결과 self의 일련번호와 동일
print(f"item1 객체의 일련번호 : {id(item1)}\n")  # \n을 추가하면 한 줄 띄어서 출력

item2 = Stock2('SK텔레콤', 238000, 20)

print(f"item2 객체의 일련번호 : {id(item2)}\n")

item3 = Stock2('현대자동차', 165500, 3)
print(f"item3 객체의 일련번호 : {id(item3)}\n")

print("\n*************************************ex4*************************************")

'''
클래스: 속성(상태)과 기능(동작)의 정의로 이루어져있다.  
객체: 클래스의 정의로 생성된 대상이다. 

객체의 특징인 속성은 변수로, 객체가 할 수 있는 일인 기능은 메서드로 구현되어있다.
즉, 객체는 클래스의 정의대로 변수와 메서드의 묶음으로 이루어져있다.

ex1) 객체가 주식종목 이라면 stock_name(종목명), price(현재가), rate(수익률)과 같은 속성은 변수로 구현하고
print(출력), change_price(가격 변경)과 같은 기능(동작)은 메서드로 구현
ex2) 객체가 자전거라면 바퀴의 크기, 색깔 같은 속성은 변수로 구현하고
전진, 방향 전환, 정지 같은 기능(동작)은 메서드로 구현

클래스든, 메서드든 호출 되기 전에는 실행 되지 않는다.
'''


class Stock3:
    def __init__(self, stock_name, stock_price, stock_rate):
        self.name = stock_name  # 인스턴스변수 : self.name, self.price, self.rate를 인스턴스 변수라고 한다.
        self.price = stock_price
        self.rate = stock_rate

    def print(self):  # 메서드(method = function) : 클래스 내부에 정의 된 함수
        # 인스턴스 변수는 class 내의 다른 메서드에서 사용 가능
        print(f"stock_name: {self.name}, price: {self.price}, rate: {self.rate}")

    def change_price(self, new_price):
        self.price = new_price


item1 = Stock3('삼성전자', 60900, 3.5)
item2 = Stock3('SK텔레콤', 238000, 20)
item3 = Stock3('현대자동차', 165500, 3)

item1.print()
item2.print()
item3.print()

# item1 객체의 chage_price 메서드를 활용해 price 속성 변경
item1.change_price(61000)
item1.print()

print("\n*************************************ex5*************************************")

'''
[계산기 프로그램 만들기 예제]
class : 붕어빵 틀
즉, Calculator는 붕어빵 틀
'''


class Calculator:
    def __init__(self, first, second):
        # self.x, self.y  : instance 변수
        self.x, self.y = first, second

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def mod(self):
        return self.x / self.y


# ctrl을 누른 상태로 함수, 변수 클릭 하면 선언부로 이동
# ctrl + alt + 왼쪽, 오른쪽 방향키 : 이전 커서

# cal1 객체에는 x에 1을, y에 2를 넣음(cal1 객체는 init 생성자의 self와 동일, 1은 fisrt 매개변수로 전달, 2는 second로 전달
cal1 = Calculator(1, 2)

# cal2 객체에는 x에 3을, y에 4를 넣음
cal2 = Calculator(3, 4)

# cal1라는 객체의 add 메소드를 호출하고 return(반환) 되는 self.x + self.y 결과가 answer라는 변수 안에 저장 된다.
answer = cal1.add()
print("answer : ", answer)

# 위에서는 cal1.add() 의 결과를 answer에 담고 answer를 출력했지만, 변수에 담지 않아도 바로 return 결과를 출력 할 수 있다.
print("cal1.add() : ", cal1.add())

# 똑같이 add() 메소드를 호출 했지만, 3,4 라는 다른 팥을 위에서 넣었기 때문에 다른 결과가 출력 된다.
print("cal2.add() : ", cal2.add())
print("cal1.sub() : ", cal1.sub())
print("cal2.sub() : ", cal2.sub())
print("cal1.mul() : ", cal1.mul())
print("cal2.mul() : ", cal2.mul())
print("cal1.mod() : ", cal1.mod())
print("cal2.mod() : ", cal2.mod())

print("\n*************************************ex6*************************************")
'''
__init__에 매개변수가 없을 경우?
'''


class Ex6:
    def __init__(self):
        # self.x, self.y  : instance 변수
        self.x, self.y = 1, 2


c = Ex6()
print(f" c.x: {c.x}")
print(f" c.y: {c.y}")

print("\n*************************************ex7*************************************")
'''
class 안에서 객체 생성 예제
'''


class Test:  # Test 이라는 이름을 가진 클래스를 정의
    def __init__(self, tx, ty):  # 메서드(method = function) : 클래스 내부에 정의 된 함수
        self.x = tx  # 인스턴스변수 : self.name, self.price, self.rate를 인스턴스 변수라고 한다.
        self.y = ty


class Test2:
    def __init__(self):
        self.item = Test(1, 2)

    def print(self):
        print(f"self.item.x : {self.item.x}, self.item.y : {self.item.y}")


t = Test2()
t.print()
print(f"t.item.x : {t.item.x}, t.item.y : {t.item.y}")


