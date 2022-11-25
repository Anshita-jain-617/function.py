# Q39. Your task is to make two functions, max and min (maximum and minimum in PHP and Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
# #Examples:-

# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5.


# minimun([42, 54, 65, 87, 0]) returns 0.


def list(a):
    i=0
    max=0
    min=a[i]
    while i<len(a):
        if max<a[i]:
            max=a[i]
        if min>a[i]:
            min=a[i]
        i+=1
    print("max",max,"min",min)
list([4,6,2,1,9,63,-134,566])