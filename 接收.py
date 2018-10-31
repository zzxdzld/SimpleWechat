from itchat.content import *
import time
from datetime import *
import ende
import threading
itchat.auto_login(enableCmdQR=False)#hotReload=True
@itchat.msg_register(TEXT) 
def print_content(msg): 
	global username
	username=msg["FromUserName"]
	de_textt=ende.de_code(msg["Text"])
	print("["+username+"]>>>"+de_textt+"\n按回车键回复")
def replymsg():
	global username 
  	while True: 
 		textt=input("[你]>>>") 
 		en_textt=ende.return_text(textt) 
 		itchat.send(en_textt,toUserName=username)
 		t = threading.Thread(target=itchat.run)
 		t2= threading.Thread(target=replymsg)
t.start()
t2.start()
t.join()
t2.join()