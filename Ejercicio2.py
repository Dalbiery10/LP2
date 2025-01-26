#ejercicio 1

n = int(input("Ingresa un número entero: "))

total = len(str(abs(n)))

print(f"El número tiene {total} dígitos.")


#ejercicio 2

num = int(input("Dime un número entero: "))
if num > 1:
    es_primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            es_primo = False
            break
    print(f"{num} es primo." if es_primo else f"{num} no es primo.")
else:
    print(f"{num} no es primo.")


#ejercicio 3
numeros = [int(input(f"Número {i + 1}: ")) for i in range(4)]
mayor = numeros[0]
posicion = 0
for i in range(len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i
print(f"El mayor es {mayor} en la posición {posicion}.")



#ejercicio 2
num = [1, 1, 2, 3, 3, 2, 5, 6, 2, 7, 8, 4, 3, 1]

resultado = list(set(num))

print("Lista sin duplicados:", resultado)
