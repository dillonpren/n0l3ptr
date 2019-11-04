s='this_is_not_the_flag'
f=open('XORcute-able.flag').read()
f=f.split('\n')[0]
s=s[::-1]
f=f[::-1]
b=''
for i in range(20):
 b+=chr(ord(s[i])^ord(f[i]))
print(b[::-1])

