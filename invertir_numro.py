# programa para invertir un numero de cuatro digitos

# input
n = input("Digite un numero de cuatro digitos: ")
n = int(n)

# processing
r4 = n%10
r3 = (n//10)%10
r2 = (n//100)%10
r1 = (n//1000)%10

ni = r4*1000 + r3*100 + r2*10 + r1

# output
print("-----resultados-----")
print("numero original: " + str(n))
print("ultimo digito: " + str(r4))
print("tercer digito: " + str(r3))
print("segundo digito: "+ str(r2))
print("primer digito: " + str(r1))
print("El numero invdertido es: " + str(ni))