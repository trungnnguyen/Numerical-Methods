# To find the activation energy(E) and the rate constant (C_a*K_o)
#Data for the given equation is available
#rate=C_a*K_oexp(-E/RT) (equation)

import matplotlib.pyplot as plt
import math

def delete_first_element(a,log_rate,inv_Temp):
    #To remove first two lines of text
    a.pop(0)
    log_rate.pop(0)
    inv_Temp.pop(0)
    
def input_file(file_data):
    #To retreive only the relevant data from the file.
    #Data returned in a form to be used in a polynomial.
    file_data=open(file_data,'r')
    a=[]
    inv_Temp=[]
    log_rate=[]
    for line in file_data:
        line=line.replace("\t"," ")
        line=line.replace("\n","")
        a.append(line.split(" "))
        log_rate.append(0)
        inv_Temp.append(0)
    delete_first_element(a,log_rate,inv_Temp)
    delete_first_element(a,log_rate,inv_Temp)
        
    for i in range(0,len(a)):
        inv_Temp[i]=1.0/(float(a[i][0]))
        log_rate[i]=math.log(float(a[i][1]))
        
    del a
    return log_rate,inv_Temp

def weights(inv_Temp):
#Weights to be assigned for weighted least square.
    w=[]
    for wi in range(0, len(inv_Temp)):
        w.append(1)
    return w

def matrix_form(log_rate, inv_Temp,w):
    #Obtaining the matrix which can be used to solve the coefficients of the polynomial equation
    #based on the degree of the polynomial
    y=log_rate
    x=inv_Temp
    n=int(raw_input('Degree of polynomial: '))
    B=[]
    
    for i in range(0,n+1):
        b=[]
        for j in range(0,n+2):
            b.append(0)
        B.append(b)
	
	#Filling the matrix to solve the polynomial        
    for j in range(0,n+1):
        for k in range(0,n+1):
            sum1=0
            if(k<=j):
                for i in range(0,len(w)):
                    sum1=sum1+w[i]*(x[i]**(j+k))
                B[j][k]=sum1
                B[k][j]=B[j][k]  
                
   #Filling the experimental output from the data             
    for j in range(0,n+1):
        k=n+1
        sum2=0
        for i in range(0,len(w)):
            sum2=sum2+w[i]*y[i]*(x[i]**j)
        B[j][k]=sum2

    return B,n

def solver(A,n):
    #Get coefficients of the polynomial from the matrix B
    a=[]
    for i in range(0,n+1):
        a.append(1)
    for i in range(0,n+1):
        for j in range(0,n+1):
            if(i!=j):
                k=A[j][i]/A[i][i]
                for l in range(0,n+2):
                    A[j][l]=A[j][l]-k*A[i][l]
    for i in range(0,n+1):
        a[i]=float(A[i][n+1]/A[i][i])    
    return a # coefficients of the polynomial equation

file_data='input-WLS.txt'
log_rate, inv_Temp=input_file(file_data)
w=weights(inv_Temp)
B,n=matrix_form(log_rate,inv_Temp,w)
a=solver(B,n)

rate_constant=math.exp(a[0])
R=8.314
activation_energy=-a[1]*R

print 'The rate constant is '+str(rate_constant)+ ' mole/Lmin'
print 'The activation energy is '+str(activation_energy)+' J/mol'
