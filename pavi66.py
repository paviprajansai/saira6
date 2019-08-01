n11=int(input())
for i in range(2,n11):
  if n11%i==0:
    flag=0
    break
  else:
    flag=1
if flag==1:
  print("yes")
else:
  print("no")
  #i
