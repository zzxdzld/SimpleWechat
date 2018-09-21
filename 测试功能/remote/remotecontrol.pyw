#encoding:utf8
import itchat
import os
import time
import cv2 #如果使用opencv的话可以远程拍照
import caution as c

sendMsg = u"[消息助手]:暂时无法回复" #自动回复内容
usageMsg = u"""使用方法：
1.运行CMD命令：cmd xxx (xxx为命令)
2.获取电脑截图：截图
3.关闭消息助手：关闭
4.远程关闭电脑：关机"""
c.__init__()
@itchat.msg_register('Text') #注册文本消息
 
def text_reply(msg): #心跳程序
    global flag
    message =  msg['Text'] #接收文本消息
    fromName =msg['FromUserName'] #发送方
    toName = msg['ToUserName'] #接收方
 
    if toName == "filehelper":
        if message == "截图": #远程拍照并发送到手机
            from PIL import ImageGrab
            im = ImageGrab.grab()
            im.save('weixinTemp.jpg','jpeg')
            itchat.send('@img@%s'%u'weixinTemp.jpg','filehelper')
        if message[0:2] == "cmd": #远程执行cmd命令 
                os.system(message.strip(message[0:3])) #远程执行cmd命令，可以实现关机
        if message == "关机":
            os.system("shutdown -s -t 0")
        if message == "关闭":
            flag = 0
            itchat.send("消息助手已关闭","filehelper")
            exit()
        if message == "":
            #python + opencv 实现屏幕录制
            from PIL import ImageGrab
            import numpy as np
            import cv2
            screen = ImageGrab.grab()#获得当前屏幕 
            length,width=screen.size#获得当前屏幕的大小
            video_decode_style = cv2.VideoWriter_fourcc(*'XVID')#编码格式
            video = cv2.VideoWriter('a.avi', video_decode_style, 32, (length, width))#输出文件命名为a.mp4,帧率为32，可以调节
            while True:
                im = ImageGrab.grab()
                imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
                video.write(imm)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            video.release()
            cv2.destroyAllWindows()
            itchat.send('@vid@%s' % 'a.avi')
    elif flag==1:
        itchat.send(sendMsg,fromName)
        myfile.write(message) #保存消息内容 
        myfile.write("\n")
        myfile.flush()
flag = 0
nowTime = time.localtime()
filename =str(nowTime.tm_mday)+str(nowTime.tm_hour)+str(nowTime.tm_min)+str(nowTime.tm_sec)+".txt"
myfile = open(filename,'w')
 
if __name__ == '__main__':
    itchat.auto_login()
    itchat.send(usageMsg,"filehelper")
    itchat.run()
