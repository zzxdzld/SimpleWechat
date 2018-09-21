from itchat import *
from tkinter import *
def a():
	root=Tk()
	Label(root,text="对方的用户名：").grid(row=0)
	Label(root,text="发给对方的消息：").grid(row=1)
	name=StringVar()
	msg=StringVar()
	e1=Entry(root,textvariable=name)
	e2=Entry(root,textvariable=msg)
	e1.grid(row=0,column=1,padx=10,pady=5)
	e2.grid(row=1,column=1,padx=10,pady=5)
	def show():
		e1.delete(0,END)
		e2.delete(0,END)
		root.quit()
	Button(root,text='继续',width=37,command=show)\
.grid(row=2,column=1,sticky=W,padx=0,pady=5)
	mainloop()