for i in range(0,80):
	a=i
	if(i%4==0):
		a='linked'
	if(i%6==0):
		a='in'
	if((i%4==0) and (i%6==0)):
		a='linkedin'
	print a
