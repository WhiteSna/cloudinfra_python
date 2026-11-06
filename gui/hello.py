# gui/hello.py


# as 별칭을 tk로 부여하겠다는 의미
import tkinter as tk


if __name__ == "__main__":
    # Tk 객체 생성해서 참조값을 root에 담기
    root = tk.Tk()
    root.geometry("300x100")
    
    lable = tk.Label(root, text="Hello, tkinter!", font=("Arial", 14))
    lable.pack(pady=30)
    
    root.mainloop()