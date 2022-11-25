def unique_num(a):
    i=0
    b=[]
    while i<len(a):
        if a[i] not in b:       
            b.append(a[i])
        i+=1
    print(b)
unique_num([1,2,3,3,4,5,2,6,4])
