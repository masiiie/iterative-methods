import time, threading, sys

def Seidel(M,b,presicion):
    sol = Array(len(M),0)
    anterior = Array(len(M),0)
    error = Array(len(M),8000000000)
    iteraciones = 0
    b = B(M)
    r = b/(1-b)
    t = r*Norma(error)
    print("b de M es ",b)

    while(t > presicion):
    	print(iteraciones)
    	mult = MultSeidel(M,anterior)
    	sol = Suma(mult,b)
    	error  = Resta(sol,anterior)
    	ne = Norma(error)
    	t = r*ne
    	print("solucion ",sol)
    	Copiar(sol,anterior)
    	iteraciones += 1
    print("Seidel ",iteraciones," iteraciones\n")
    return sol

def MultSeidel(M,mult):
    for i in range(0,len(M)):
    	mult[i] = 0
    	for j in range(0,len(M)):
    		mult[i] += M[i][j]*mult[j]
    return mult

def B(M):
	p = P(M)
	q = Q(M)
	b = -1

	for i in range(0,len(M)):
		c = q[i]/(1 - p[i])
		if(c > b): b = c
	return b  

def P(M):
	p = Array(len(M),0)
	for i in range(0,len(M)):
		for j in range(0,i):
			if(M[i][j]>0):
				p[i]+=M[i][j]
			else:
				p[i]-=M[i][j]
	return p

def Q(M):
	q = Array(len(M),0)
	for i in range(0,len(M)):
		for j in range(i + 1,len(M)):
			if(M[i][j]>0):
				q[i]+=M[i][j]
			else:
				q[i]-=M[i][j]
	return q


def Jacobi(M,b,presicion):
    sol = Array(len(M),0)
    anterior = Array(len(M),0)
    error = Array(len(M),8000000000)
    iteraciones = 0
    a = NormaMatriz(M)
    r = a/(1-a)
    t = r*Norma(error)
    print("La norma de M es ",a)
    v = 8

    while(t > presicion):
    	print(iteraciones)
    	mult = Multiplicacion(M,anterior)
    	sol = Suma(mult,b)
    	error  = Resta(sol,anterior)
    	ne = Norma(error)
    	t = r*ne
    	print("solucion ",sol)
    	Copiar(sol,anterior)
    	iteraciones += 1
    print("Jacobi ",iteraciones," iteraciones\n")
    return sol

def Copiar(a,b):
    for i in range(0,len(a)):
        b[i] = a[i]
    return 0

def Norma(x):
    max = -1
    for i in range(0,len(x)):
        if(x[i]>max):
            max = x[i]
    return max

def NormaMatriz(M):
    max = -1
    for i in range(0,len(M)):
        suma = 0
        for j in range(0,len(M)):
            if(M[i][j] > 0):
                suma += M[i][j]
            else:
                suma -= M[i][j]
        if(suma > max): max = suma
    return max

def Suma(a,b):
    suma = Array(len(a),0)
    for i in range(0,len(a)):
        suma[i] = a[i] + b[i]
    return suma


def Resta(a,b):
    suma = Array(len(a),0)
    for i in range(0,len(a)):
        suma[i] = a[i] - b[i]
    return suma

def Multiplicacion(M,x):
    mult = Array(len(M),0)
    for i in range(0,len(M)):
        for j in range(0,len(M)):
            mult[i] += M[i][j]*x[j]
    return mult

def Array(a,valor):
    sol = []
    while a:
        sol.append(valor)
        a = a-1
    return sol

M = [[0,1/10,-1/5],[1/5,0,1/5],[-1/4,1/8,0]]
b = [3/5,2,-1]
print(Jacobi(M,b,0.01))
