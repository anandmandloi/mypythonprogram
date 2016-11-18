
def findinv(a,p):#finds inverse
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
def crt(a,m,b,n,c,max):
	if (a,m)==(-1,-1):
		a=int(input())
		m=int(input())
		return crt(a,m,b,n,c+1,max)
	if c==max:
		return a
	else:
		b=int(input())
		n=int(input())
		p=(((b-a)%n)*findinv(m,n))%n
		x=p*m+a			
		return crt(x,m*n,b,n,c+1,max)
print("enter the no. of simultaneous equations in hand")
t=int(input())
print(crt(-1,-1,-1,-1,0,t))
