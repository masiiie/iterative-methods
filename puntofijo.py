def g(x):
	return sqrt
def Puntofijo(x):
	y = g(x)
	while(y!=x):
		x = y
		y = g(x)
	return y