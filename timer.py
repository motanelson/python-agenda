#!/usr/bin/python
import time;
def gettimes():
	return time.time();
def report(t):
	local=time.asctime(time.localtime(t));
	print (local);
def add(a,b):
	return a+b;
sseconds=12;
print("\033c\033[42;30m\n");
t=gettimes();
report(t)
tt=add(gettimes(),sseconds);
report(tt);
print("waiting for future event");
while t<tt:
	t=time.time();
#print add(10,10);