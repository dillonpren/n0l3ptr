s=open('flag.txt').read()
s=s.split('\n')[0]
s=s.split('20')
dec=''
for x in s:
  dec+=chr(int(x,16))
print dec
