# Step14_file2.py

import os

if __name__ == "__main__":
    
    # 새로운 파일을 만들어서 문자열을 파일에 출력하기
    
    letter_path = os.path.join(os.getcwd(), "memo.txt")
    
    with open(letter_path, "w", encoding="utf-8") as f:
        f.write("To my Friend \n")
        f.write("Hello \n")
        f.write("Bye \n")
        