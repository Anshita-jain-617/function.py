# Q30. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter



n=int(input("Enter the number till you want to check: "))
primes = []
for i in range (2, n+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        primes.append(i)
print(primes)




