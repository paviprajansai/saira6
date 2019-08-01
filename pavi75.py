s11=input()
k11=list(s11)
for i in range(0,len(k11)):
    if i==int(len(k11)/2):
        k11[i]="*"
        if len(k11)%2==0:
            k11[i-1]="*"
print("".join(k11))
