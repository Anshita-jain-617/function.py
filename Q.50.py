# # Q50. Make a split function
# # Input :-[“i am anjali”]
# # Output :- [‘i’,’am’,’anjali’]

# def split(a):
#     pri




a="my name is anshita"
i=0
b=[]
c=""
while i<len(a):
    if a[i]=="":
       c+=a[i-1]
       b.append(c)
    i+=1
print(b)

