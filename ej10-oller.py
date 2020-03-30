num = int(input("Ingresa un numero entero positivo mayor que 2: "))
i = 2
while num % i != 0:
    i += 1
if i == num:
    print(str(num) + " es primo")
else:
    print(str(num) + " no es primo")