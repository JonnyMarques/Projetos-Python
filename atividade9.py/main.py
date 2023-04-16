from functools import reduce

x = range(10)

def somar(x,y):

    return x+y

x = [i**2 for i in x if i%2==0]

reduce(somar, x)


print (somar())