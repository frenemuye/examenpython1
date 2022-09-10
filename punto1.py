# 1.Construir un programa que permita ingresar N (cantidad digitada por el usuario) 
# números enteros y cuente cuantos múltiplos de 2 y de 3 fueron ingresados (+1)

import os
os.system ("cls")

numbers = []
de3=[]
de2=[]
x=0
y=0
n=int(input("Digita limite: "))

for i in range(n):    
    numbers.append(int(input(f"Digita valor {i}: ")))
    if numbers[i]%2==0:
        de2.append(numbers[i])
        x=x+1
    if(numbers[i]%3==0):
        de3.append(numbers[i])
        y=y+1
print("")
print("")

print("valores del vector")
i=0
for i in range(n):    
    print(f'vector [{i}] tiene {numbers[i]}')
print("")
print("")

print("valores multiplos de 2")
i=0
for i in range(x):    
    print(f'vector [{i}] tiene {de2[i]}')
print("")
print("")

print("valores multiplos de 3")
i=0
for i in range(y):    
    print(f'vector [{i}] tiene {de3[i]}')


