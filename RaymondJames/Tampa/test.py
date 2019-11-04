import base64
s=open('test.pcap').read()

i=0
pck=[]
s=s[40:]
for i in range(79):
 pck.append(s[:1500])
 s=s[1516:]

for i in range(len(pck)):
 pck[i]=base64.b64decode(pck[i][42:]+'==')

#for i in range(len(pck)):
# print 'Pack {}:'.format(i)
# print pck[i]

txt=[]
for i in range(75):
 txt+=pck[i]
print ''.join(txt)
#print pck[1]
#print pck[74]
