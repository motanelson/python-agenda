#!/usr/bin/python
import thread;
import time;
from datetime import datetime;
lists=[];
def gettimes():
	t=time.time();
	return t;
def report(t):
	local=time.asctime(time.localtime(t));
	print (local);

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
		t=time.strptime(a,"%m/%d/%y %H:%M:%S");
		t=time.mktime(t);
		print(t);
		report(t);
		lists+=[t];

		
def add(a,b):
	return a+b;
n=0;
t=0.00;
l=0;
print("\033c\033[42;30m\n");
report(gettimes());
thread.start_new_thread(inputs,())
while 1:
	l=len(lists);
	if l>0:
		t=gettimes();
		for n in range(0,l):
			if lists[n]<t:
				print("alert:");
				report(lists[n]);
				lists.remove(lists[n]);

