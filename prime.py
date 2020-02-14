import math
print("program to check prime number ");
n=int(input("Enter a number: "));
flag=0
if n>1:
	for i in range(2,(int)(math.sqrt(n))):
		if n%i==0:
			flag=1
else:
	flag=1;
if flag==1:
	print(n,"is not prime")
else:
	print(n," is prime")
