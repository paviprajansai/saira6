s11=input()
for i in s11:
	if i=="a" or i=="e" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i=="U":
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
  #i
