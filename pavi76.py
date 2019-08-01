n11=int(input())
for  i11 in range(2,n11):
	if n11%i11==0:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
  #i
