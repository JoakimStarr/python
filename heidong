def heidong(x):
	i=0
	while True:
		a=x//100
		r=x%100
		b=r//10 
		c=r%10
		if a < b:
			t=a
			a=b 
			b=t 
		if a < c:
			t=a 
			a=c 
			c=t
		if b < c:
			t=b 
			b=c 
			c=t 
		m=100*a+10*b+c 
		n=100*c+10*b+a
		x=m-n
		i=i+1
		print(i,a,b,c,x)
		if x == 495:
			print(i)
			return
heidong(907)
