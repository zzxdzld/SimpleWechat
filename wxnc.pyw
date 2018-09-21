from itchat import *
import easygui as e
from tkinter import *
import sys
import gui
def text():
  auto_login(hotReload=False)
  what="U"
  while what!=0:
    what=eval(e.enterbox("[0] 退出程序\n[1] 发送消息"))
    if what==1:
      gui.a()
      user=search_friends(name=gui.name[0]['UserName'])
      mess=gui.msg
      for x in range(time):
        send(mess,user)
    elif what==0:
      sys.exit(0)
text()
