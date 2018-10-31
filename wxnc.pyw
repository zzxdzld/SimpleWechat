from itchat import *
import sys
import gui
import easygui as e
def text():
  auto_login(hotReload=False)
  what=e.choicebox(['显示文档','发送消息'])
  while what!=0:
    if what==1:
      list1=gui.a()
      user=search_friends(name=list1[0][0]['UserName'])
      mess=list1[1]
      for x in range(time):
        send(mess,user)
      print(list1)
    elif what==0:
      sys.exit(0)
text()