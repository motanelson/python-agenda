#!/usr/bin/python
import thread;
import time;
from datetime import datetime;
from Tkinter import *
import tkMessageBox;
lists=[];
def gettimes():
	t=time.time();
	return t;
def report(t):
	local=time.asctime(time.localtime(t));
	print (local);
def msgboxs(t):
        s="time: "
        s = s + time.asctime(time.localtime(t));
	root=Tk();
	ss=StringVar();
	ss.set("time:                       ");
	label=Label(root,textvariable=ss,font="mono",justify="left").pack()
        ss.set(s);
	root.mainloop();
def inputs():
	a="";
	global lists;
	t=0;
	t=gettimes();
	while 1:
		print("month/day/year hors:minuts:seconds")
		a=raw_input();
		t=0.00;
		t=gettimes();
		try:
			t=time.strptime(a,"%m/%d/%y %H:%M:%S");
			t=time.mktime(t);
			print(t);
			report(t);
			lists+=[t];
		except:
			print("data not correct");
def add(a,b):
	return a+b;
n=0;
t=0.00;
l=0;
tt=0.00;
print("\033c\033[42;30m\n");
report(gettimes());
thread.start_new_thread(inputs,())
while 1:
	l=len(lists);
	if l>0:
		t=gettimes();
		for n in range(0,l):
			if lists[n]<t:
				tt=lists[n];
				lists.remove(lists[n]);
				msgboxs(tt);
