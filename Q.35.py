# Q35. Kids drink toddy.
#         Teens drink coke.
#         Young adults drink beer.
#         Adults drink whisky.
#         Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".




# def drink(age):
#     if age<=14:
#         print("can drink toddy")
#     elif age>=14 and age<18:
#         print("can drink coke")
#     elif age>=18 and age<21:
#         print("can drink beer")
#     else:
#         print("can drink whisky")
# drink(int(input("enter age")))






# Q37. Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,
# [True,  True,  True,  False,
# True,  True,  True,  True ,
# True,  False, True,  False,
# True,  False, False, True ,
# True,  True,  True,  True ,
# False, False, True,  True]

# The correct answer would be 17.Hint: Don't forget to check for bad values like null/undefined.

def list(a):
    i=0
    c=0
    while i<len(a):
        if a[i]==True:
            c+=1
        i+=1
    print(c)
list([True,  True,  True,  False,
True,  True,  True,  True ,
True,  False, True,  False,
True,  False, False, True ,
True,  True,  True,  True ,
False, False, True,  True])
            