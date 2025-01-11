def facto(n):
	if n<0:
		return 'ERROR'
	elif n ==0 or n==1:
		return 1
	else:
		return n*facto(n-1)

def facto_i(n) :
	cont=1
	for i in range(1,n+1):
		cont*=i
	return cont

x=int(input('Ingrese un numero entero: '))
#print('El Factorial de x es: ', facto(x))

print('El Factorial de x es: ', facto_i(x))


