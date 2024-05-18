#python program to list all the prime numbers in given interval

lower=int(input("enter the lower number:"))
upper=int(input("enter the upper number:"))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)