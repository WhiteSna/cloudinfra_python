# Step04_Str3.py

# yaml 문자열응ㄹ 다룰때는 외부 모듈을 pip로 설치 해서 import 해야한다.
# Python 가상환경을 구성하고 pip install pyyaml 설치 후에 yaml을 다룰 수 있다.

import yaml

# yaml 형식의 문자열 작성해보기
info = '''
name: 이정호
addr: 노량진
foods: 
  - 맥주
  - 베이컨
isMan: True
body:
  weight: 75
  height: 172
'''

result = yaml.safe_load(info)
print(result)

# dict type을 다시 yaml 형식의 문자열로 변환하기
result2 = yaml.dump(result, allow_unicode=True, sort_keys=False)
print(result2)