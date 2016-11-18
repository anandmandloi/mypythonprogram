import math
def isprime( n):	#this function returns 1 if n is prime else 0			
	for i in range(2,math.floor(n**(1/2))+1):
		if n%i==0:
			return 0
	return 1
def findprime( p):#this finds a large prime below 
	maxj=myi=0
	for i in range(p-1,1,-1):
		
		if isprime(i):
			for j in range(2,math.floor(p/2)+2):#this loop checks if j is order or not.
				if modexp(i,j,p)==1:
					if maxj<j:
						maxj=j	#stores the, so far,  highest order 
						myi=i #this stores the i with above j
					break
			if j>math.floor(p/2):
				maxj=p
				myi=i
				break
	if myi==0: 
		print('myi = 0!!!')
	
	return [myi,maxj]
				
def findinv(a,p):
	if a==1:
		return 1
	s0=0
	t0=1
	s1=1
	t1=-(p//a)
	r0=a
	r1=p%a
	while r1!=1:
		q=r0//r1
		temp=r0
		r0=r1
		r1=temp%r1
		templ=[s1,t1]
		s1=s0-q*s1
		t1=t0-q*t1
		[s0,t0]=templ
	
	return t1
				
def modexp(i,j,p):	#raises i to the power j mod p
	temp=1
	if j==0:
		return 1
	for c in range(1,j+1):
		temp=(temp*i)%p
	return temp
#############################################################################################

p=int(input()) #this is the no. modulo which we work..

h=int(input())	#this is the no. whose log we need to find

#also i've achieved base for log using a function that yields best candidate (one with max order).
 
l=findprime(p)

g=l[0]
print('found g!! its '+str(g)+" and it's order is "+str(l[1]))

n=math.floor(l[1]**(1/2)+1)
sb=[modexp(g,i,p) for i in range(1,n+2)]	#in this list, 1 is not included on purpose
sg=[(h*findinv(modexp(d,n,p),p))%p for d in sb] 	#see if i dint use the upper list in this list,the whole purpose of this algo is lost!!
sb.append(1)	#now adding 1 to sb 

#i don't need the matchin value but power corresponding to that, suggesting dict, but forturnately 
#the comprehension is pretty straight in iteration so i can work without dict( actually findin key 
#from value is a difficult job in python(as far as i know...).)

sbs=set(sb)
sgs=set(sg)
nsbgs=sbs&sgs     #The and
lis=list(nsbgs)
print(lis)
x=lis[0]
xbin=sb.index(x)
xgin=sg.index(x)
xbin=xbin+1 #indices start at 0
 
xgin=xgin+1
print('aaaand ..\a\a\a the log  is')
print((xbin+n*xgin)%(p-1))
 


