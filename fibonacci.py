Numero=int(input('Ingrese el numero limite: '))
Fibonacci=[1,1]
i=2
while Fibonacci[i-2]+Fibonacci[i-1]<=Numero:
    Fibonacci.append(Fibonacci[i-2]+Fibonacci[i-1])
    i+=1
print(Fibonacci)

