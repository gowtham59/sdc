r1,b2=map(int,input().split())
N3=[]
for z in range(r1,b2+1):
    for p in range(2,z):
        if(z%p==0):
            break
    else:
        N3.append(z)
print(len(N3))
