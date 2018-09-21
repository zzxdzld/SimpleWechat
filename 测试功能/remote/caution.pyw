from tkinter import *
def __init__():
    window=Tk()
    window.title("Login")
    label=Label(window, text="""欢迎使用简单微信的远程电脑控制功能，
稍后会弹出一个QR码，扫后便可以登入微信了。
""", fg="black", bg="sliver", font=("Microsoft JhengHei", 18), width=60, height=10)
    label.pack()
    window.mainloop()
