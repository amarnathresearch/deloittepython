# Recursion

# Fibonacci series

def fib(x):
    if x==1 or x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(7))

def fibo(n): 
    if n <= 1:  
        return n  
    else:  
        return(fibo(n-1) + fibo(n-2))

print(fibo(7))

def rec(a):
    if a==1 or a ==2:
        return 1
    else:
        return rec(a-1)+rec(a-2)
print(rec(7))
