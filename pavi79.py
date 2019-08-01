n11,m11=map(int,input().split())
a11=n11*m11
for i in range(1,1000):
	if (i*i)==a11:
		flag=0
		break
	else:
		flag=1
if a11==0:
	print("yes")
elif flag!=0:
	print("no")
elif flag==0:
	print("yes")
	#i
