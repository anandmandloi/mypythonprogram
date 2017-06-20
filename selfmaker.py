import os
p=0
fileo=open("selfmaker.py","r")
if fileo:
	print(p)
fileo.seek(12)
stri=fileo.readlines(1)
stri=stri[0].rstrip()

fileo.seek(0)
strilis=fileo.readlines()

q=(int(stri))
fileo.close()
fileo=open("selfmaker.py","w")
strilis[1]="p=%d\n"%(q+1)
fileo.writelines(strilis)
#fileo.seek(12)
#st=
fileo.close()
#print("here")
eval("os.system('python selfmaker.py')")