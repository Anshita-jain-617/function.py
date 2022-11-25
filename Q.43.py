# Q43.  Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’].
# Print the last ‘N’ elements of the given list. ‘N’ is accepted from the user.
# Sample Input:
# 1
# Sample Output:
# q
# Sample Input:
# 3
# Sample Output:
# 5
# b
# q


def list(a):
    n=int(input("enter"))
    i=-1
    b=[]
    while i>=n:
        b.append(i)
        i-=1
    print(b)
list(['a',1,'2',5,'b','q'])
