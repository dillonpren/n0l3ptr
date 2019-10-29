#! /usr/bin/env python2
import time
import telnetlib
import webbrowser
import binascii

url=telnetlib.Telnet('misc.ctf.nullcon.net',6001)

i=1
while(True):
	print i
	s=url.read_until('--- press Enter to continue ---')
	print s
	#user=raw_input()
	url.write('\n')
	#url.write('\n')
	s=url.read_until('--- Type Answer to provided captcha')
	url.read_until('\n')
	print s
	s=s.split('\n')[1]
	f=open('hex.png','w')
	f.write(binascii.unhexlify(s))
	f.close()
	webbrowser.open('hex.png')
	user=raw_input()
	print user
	url.write(user+'\n')
	i+=1
