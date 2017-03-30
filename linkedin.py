for i in range(0,20):
	a=i
	if(i%4==0):
		a='linked'
	if(i%6==0):
		a='in'
	if((i%4==0) and (i%6==0)):
		a='linkedin'
	print a

def fizzbuzz():

	for i in range(0,20):
		b=i
		if(i%4==0):
			b='fizz'
		if(i%6==0):
			b='buzz'
		if(i%4==0) and (i%6==0):
			b='whizz'
		print b

fizzbuzz()
