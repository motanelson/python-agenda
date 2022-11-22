from Tkinter import *;
import thread;
import time;
import os;
from datetime import datetime;
t=1;
root=Tk();
root.title("agenda");
root.geometry("500x300");
frame=Frame(root);
frame2=Frame(root);
global ss;
ss=StringVar();
ss.set(" ");
iiput=Text(frame2);
iiput2=Entry(frame);
lists=[];
programToOpen="mousepad";
fileToOpen="agenda.txt";
filellog=">/dev/null";
ss="";
t6=0;
s="time:                         "
sss=""
ssss=""
def filesw(sss):
	f= open(fileToOpen,"a");
	f.write(sss+"\n");
	f.close;
def shells():
    dos=os.system(programToOpen+" "+fileToOpen+" "+filellog+" 2"+filellog);
def gettimes():
	t=time.time();
	return t;
def report(t):
	local="";
	local=time.asctime(time.localtime(t));
	return local;


def ups():
    global lists;
    a=iiput2.get()
    try:
        t=time.strptime(a,"%m/%d/%y %H:%M:%S");
        t=time.mktime(t);
        iiput.insert(INSERT,report(t)+"\n");
        lists+=[t];
        filesw(report(t)+"\n");
	thread.start_new_thread(shells,());
    except:
        iiput.insert(INSERT,"data not correct\n");
def clocks():
	global t;
	global lists;
	l=0;
	n=0;
	while t:
		l=len(lists);
		if l>0:
			t=gettimes();
			for n in range(0,l):
				if lists[n]<t:
					tt=lists[n];
					lists.remove(lists[n]);
					thread.start_new_thread(shells,());

iiput.width=3
iiput.height=1
iiput2.width=3
iiput2.height=1
frame.pack()
frame.width=500
frame.height=80
frame2.pack(side =BOTTOM)
frame2.width=500
frame2.height=200
sups=Button(frame,text="add",command=ups)
sups.pack(side =LEFT) 
iiput2.pack(side =LEFT) 
iiput.pack(side =BOTTOM)
ss="add: month/day/year hors:minuts:seconds\n\n"
iiput.insert(INSERT,ss)
thread.start_new_thread(clocks,())
root.mainloop()            
t=0
time.sleep(2)