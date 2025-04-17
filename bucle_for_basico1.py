#Brandon Morales 
#08/04/2025

#1
for i in range(101):
    print(i)
    
#2
for i in range(2, 501, 2):
    print(i)
    
#3
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 ==0:
        print("Ice Ice")
    else:
        print(i)
#4
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("Suma total de pares del 0 al 500000:", suma)

#5
for i in range(2024, 0, -3):
    print(i)

#6
numInicial = 3
numFinal = 10
multiplo = 6

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
        
        