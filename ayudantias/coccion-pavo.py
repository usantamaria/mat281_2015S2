import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg
import OLS as OLS

#Definicion vectores de datos:
Masa=[5.0,6,10,12,15,20,25,30]
Time=[2,2.5,3.4,3.5,4.5,5.4,5.8,7]

plt.plot(Masa, Time,'.')
plt.show()



##1.-Calculo sistema lineal var. adimensionales tiempo y Temperatura usando
#####como explicativas l, rho, K.

A=np.array([[1,-3,2],[0,1,0],[0,0,-1]])
B=np.array([[0],[0],[1]])
C=np.linalg.solve(A,B)
print("Su resultado de X, Y, Z fue con var. de escalamiento L, rho, k para t es", C)


D=np.array([[0,1,0],[1,-3,2],[0,0,-1]])
E=np.array([[1],[-1],[-2]])
F=np.linalg.solve(D,E)
print("Su resultado de X, Y,Z con var. de escalamiento L, rho, k para T es", F)

##2.-Calculo sistema lineal var. adimensionales tiempo y conductividad usando
#####como explicativas l, rho, T.
G=np.array([[0,1,1],[1,-3,-1],[0,0,-2]])
H=np.array([[0],[0],[1]])
I=np.linalg.solve(G,H)
print("Su resultado de X, Y, Z fue con var. de escalamiento L, rho, T para t es", I)
J=np.array([[0,1,1],[1,-3,-1],[0,0,-2]])
K=np.array([[0],[2],[-1]])
L=np.linalg.solve(J,K)
print("Su resultado de X, Y, Z fue con var. de escalamiento L, rho, k para k es", L)


##3.-Calculo sistema lineal var. adimensionales tiempo usando
#####como explicativas l, K, M.
M=np.array([[1,0,1],[-1,2,0],[-2,-1,0]])
N=np.array([[0],[0],[1]])
O=np.linalg.solve(M,N)
print("Su resultado de X, Y, Z fue con var. de escalamiento L, rho, M para t es", O)


#Agregando las hipotesis adicionales el teorema de Pi nos entrega las siguientes variables
#adiomensionales:
#1.-t=M^{2/3}
#2.-t=M^{1/3}
#3.-t=M^{2/5}

#Calculando las aproximaciones:

t_1=[]
t_2=[]
t_3=[]
for i in range(len(Masa)):
	t_1.append( Time[i]/Masa[i]**(2.0/3) )
	t_2.append( Time[i]/Masa[i]**(1.0/3) )
	t_3.append( Time[i]/Masa[i]**(2.0/5) )

np.array(t_1)
np.array(t_2)
np.array(t_3)


print t_1
print t_2
print t_3

#Encontrando las rectas

print OLS.OLS(Masa, Time)
print OLS.OLS(Masa, t_1)
print OLS.OLS(Masa, t_2)
print OLS.OLS(Masa, t_3)

m=np.arange(0, 35, 0.2)
plt.plot(Masa, Time,'.', color='red')
plt.plot(m, 0.19013522500554203*m+1.3391709155397913, color='red' )
plt.plot(Masa, t_1,'.', color= 'blue')
plt.plot(m, -0.00024911616787655241*m+0.71852155365011117, color='blue')
plt.plot(Masa, t_2,'.', color='yellow')
plt.plot(m, 0.038804544437704543*m+1.1162219295874647, color='yellow')
plt.plot(Masa, t_3,'.', color='green')
plt.plot(m, 0.025960341489622642*m+1.0345091298598947, color='green')
plt.show()


#Grafico de regla antigua versus regla nueva
T_minutes= [ ]
for i in range(len(Time)):
	T_minutes.append(60*Time[i])

ma=np.arange(0, 30, 0.2)
plt.plot(Masa, T_minutes,'.')
plt.plot(ma, 20*ma, '-')
plt.plot(ma, 45*ma**(0.666),'-')
plt.show()

