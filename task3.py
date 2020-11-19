a = int(input())
b = int(input())
c = int(input())
def my_func(a, b, c):
    n = min(a, b, c)
    return a + b + c - n
print(my_func(a, b, c))
    
