# Step09_if.py

'''
    임의의 숫자를 입력 받아서 입력한 수가 양수이면 "양수 입니다."를 출력하고자 한다면?
    (If 문을 사용해야 한다.)
'''

input_num = input("숫자 입력 : ")

if int(input_num) > 0:
    print("양수 입니다.")

elif int(input_num) < 0:
    print("음수 입니다.")

else:
    print("0 입니다.")


print("----------------")

# 로직이 만일 양자 택일 이라면 if else 블럭을 만들면된다.

if(input_num >0):
    pass
else:
    pass
print("종료 됩니다")
