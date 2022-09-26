from functools import reduce

Lista = [1,2,3,4,5,6,7,8,9,10]
Impares = filter(lambda x: x%2!=0,Lista)
print(list(Impares))
Suma = reduce(lambda x,y:x+y,Impares)
print(Suma)