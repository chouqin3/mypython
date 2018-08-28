f = open('text.txt','w')
s = "c:\\hoho\\fdajl"
y = s.replace("\\","/")
f.write(s + '\n')
f.write('line1\n')
f.write('line2\n')
f.write('By CXX\n')
f.close()



import tempfile
file1 = tempfile.mkdtemp( dir=None)
print (file1)