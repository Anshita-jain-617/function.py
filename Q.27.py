# Q27. Write a function for checking the speed of drivers. This function should have one parameter: speed.

# 1).If speed is less than 70, it should print “Ok”.
# 2).Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# 3).If the driver gets more than 12 points, the function should print: “License suspended”


# def function(speed):
#     if speed<70:
#         print("ok")
#     i=70
#     points=0
#     while i<=130:
#         if i%5==0:
#             points+=1
#         if points>12:
#             print("license suspended")
#         i+=5
# function(int(input("enter")))


# print("hai")
# def fun():
#     print("hello")
#     if 8<6:
#         print("hai")
#         print("h")
#     print("b")
# fun()
# print("a")
# print("b")


# def list(a,b):
#     c=[]
#     sum=""
#     i=0
#     j=-1
#     while i<len(a):
#         sum=a[i]+b[j]
#         c.append(sum)
#         i+=1
#         j-=1
#     print(c)
# list(["a","b","c","d"],["j","k","l","m"])

n=int(input("enter"))
i=0
while i<=n:
    j=1
    c=0
    while j<=n:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        print(i)
    i+=1