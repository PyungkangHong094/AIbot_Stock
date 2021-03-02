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

from my_package import sum, sub
from my_package.sum import Calculator #썸이라는 모듈안에 함수도 있고 카큘레이터에 있는 정의가 되어있다


x = sum.sum_ab(1, 2)

print (x)

y = sub.sub_ab(1,4)

print(y)





c = Calculator(1, 2)
print(f"c.sum(): {c.sum()}")




# __name__ ? => 현재 모듈의 이름을 담고있는 것

# if __name__ == '__main__':