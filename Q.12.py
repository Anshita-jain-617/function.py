# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105



def remove(a):
    i=0
    c=[]
    while i<len(a):
        while  a[i]>0 or a[i]<0:
            if a[i]%10!=0:
                c.append(a[i])
                break
            else:
                a[i]//=10
        i+=1
    print(c)
remove([1450,960000,1050,-1050])
