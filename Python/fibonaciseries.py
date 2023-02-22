def fibonacci(n):
    a,b=0,1
    while a<=n:
        print(a)
        a,b= b,a+b
fibonacci(50)

#using for loop
'''def fib(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(10)'''
