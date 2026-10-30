
# 특정 시점에 실행할 코드블럭을 함수에 모아 놓을 수 있다.

def store() :
    print("냉장고 문을 연다")
    print("음식을 저장한다")
    print("냉장고 문을 닫는다")

store()

# 함수가 리턴하는 값을 변수에 담아보면?
result = store() # None이 result에 들어간다

# 변수를 미리 만들어 두고 값을 나중에 넣고 싶으면 None을 대입해서 변수를 만들면된다.
a = None # a라는 변수를 미리 만들어 두는 방법
print("Step02_Datatype2.py 가 종료 됩니다")