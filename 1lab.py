def sosal(*rest):
    print(rest) 
    return sum(rest)

f = lambda a, b : a * b
print (f(5,6))
print (sosal(1, 2 , 3))


