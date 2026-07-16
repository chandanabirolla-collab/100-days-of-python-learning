#recursion 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(2))
print(factorial(3))
print(factorial(4))
#fibonaci
def fibonaci(m):
    if(m==0):
        return 0
    else:
        return (m-1) + (m-2)
print(fibonaci(4))