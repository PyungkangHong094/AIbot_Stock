"""
[자료형]
자료형(data type) : 데이터의 종류
 * 자료형 종류
    정수: int
    실수: float
    문자열: str
    (참, 거짓): bool

    list(리스트)
    tuple(튜플)
    set(집합, 셋)
    dict(사전, 딕셔너리)
    등등
"""

print("\n*************************************ex1*************************************")
# type() : 데이터 타입을 확인 하는 내장 함수
print("1: ", type(1))
print("1.1: ", type(1.1))
print("abc: ", type("abc"))
print("True: ", type(True))
print("False: ", type(False))

val = 123
print("type val: ", type(val))

val2 = "123"
print("type val2: ", type(val2))


print("\n*************************************ex2*************************************")
'''문자열 합치기'''

a = '안녕'
b = '하세요'
c = a + b
print(c)

print("\n*************************************ex3*************************************")
'''문자열 포맷팅'''

name = '홍길동'
print("%s님, 안녕하세요!" % name)  # 비추천, python2 버전에 사용하던 방식
print("{}님, 안녕하세요!".format(name))  # 추천
print(f"{name}님, 안녕하세요!")  # 추천 / f-string 이라고 표현 / python 3.6 이상 부터 지원
# 비교
print(name, "님, 안녕하세요!")

# "안녕하세요 홍길동님, 반갑습니다." 를 출력 하시오
print("안녕하세요", name, "님, 반갑습니다.")
print("안녕하세요 {} 님, 반갑습니다.".format(name))
print(f"안녕하세요 {name} 님, 반갑습니다.")

