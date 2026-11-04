# Step11_class.py

'''
    1. 클래스는 객체를 생성할 수 있는 설계도 역할
    2. Data type의 역할
    
    객체는 속성(저장소)와 기능(함수)로 이루어진다.
'''

# 간단한 Car 클래스 정의
class Car:
    def drive(self):
        print("달려요!")

# Car 클래스를 이용해서 객체를 생성하고 그 참조값을 c1이라는 이름의 Car type 변수에 담기
c1: Car = Car()
# c1에 .을 찍으면 해당 객체를 사용할 수 있다.
c1.drive()