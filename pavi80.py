s11=input()
l=list(s11)
s11=""
for i in range(0,len(l)):
    if int(l[i])%2!=0:
        s11=s11+l[i]+" "
print(s11.strip())
