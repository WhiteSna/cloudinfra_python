
# json 형식의 문자열을 작성하고 python에서 활용해보자
import json


info = '''
{
    "name" : "이정호",
    "addr" : "노량진",
    "foods" : ["맥주", "베이컨"]
}
'''

result = json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

# dict에 저장된 데이터를 json 문자열로 변환
result2 = json.dupms(result)

print("종료합니다")