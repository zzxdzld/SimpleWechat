import wxyc
import easygui as e
while True:
    choice = e.buttonbox('请选择服务', 'Please Choose', ('发送文本', '发送图片', '发送视频','自动回复','远程控制电脑','关闭该应用'))
    if choice == '关闭该应用':
        sure = e.ynbox('确定关闭此应用?', 'Are you sure closing this application?', ('确定', '返回'))
        if not sure:
            pass
        else:
            break
    elif choice == '发送文本':
        wxyc.text()
    elif choice == '发送图片':
        wxyc.image()
    elif choice == '发送视频':
        wxyc.video()
    elif choice == '自动回复':
        wxyc.turing()
    elif choice == '远程控制电脑':
        wxyc.rc()
