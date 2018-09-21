# coding: Utf-8
from itchat import *
import sys
def text():
  import easygui as e
  auto_login(hotReload=False)
  what="U"
  while what!=0:
    what=eval(e.enterbox("""
  [0] 退出程序
  [1] 发送消息
  [2] 显示说明
    """))
    if what==1:
      user=search_friends(name=e.enterbox("请问您要将消息发送给谁?  "))[0]['UserName']
      mess=e.enterbox("请问您要发送什么消息?  ")
      time=int(e.enterbox("请问要发送几次  "))
      for x in range(time):
        send(mess,user)
      e.msgbox("发出成功!按[OK]继续。")
    elif what==2:
      e.msgbox("该软件由Python语言编出，由itchat模块做支持。")
    elif what==0:
      sys.exit()
    elif what!=1 and what!=2 and what!=0:
      e.msgbox("错误,按[OK]退出")
      sys.exit()
def image():
  send_image()
text()
