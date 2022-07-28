#fibonacci series
# f(k)= k, if k={0,1}
# f(k)= f(k-1) + f(k-2), if k>1
# where k is always a whole number

def fib(n):
    if n <= 1:
        return n
 
    return fib(n - 1) + fib(n - 2)

print(fib(0))