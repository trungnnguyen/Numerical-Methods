from math import sqrt

n=int(raw_input('order of the matrix: '))#order of the matrix (A)

def input_A():
# Input for A,b and initializing L
    A=[]
    L=[]
    c=[]
    b=[]

    for i in range(0,n):
        for j in range(0,n):
            c.append(0)
        A.append(c)
        c=[]

    for i in range(0,n):
        for j in range(0,n):
            c.append(0)
        L.append(c)
        c=[]
    
    print "Enter the matrix A"
    print "It is a symetric matrix"

    for i in range(0,n):
        for j in range(0,i+1):
            A[i][j]=float(raw_input('A_'+str(i+1)+str(j+1)+'='))
            A[j][i]=A[i][j]
        A.append(c)
        c=[]
    

    print "Enter the vector b"

    for i in range(0,n):
        b.append(float(raw_input('b_'+str(i+1)+'=')))
        

    return b,A,L

def output_L(b,A,L):
# Finding L from A
    for k in range(0,n):
        for i in range(0,k):
            Temp=0
            if(k!=i):
                for j in range(0,i):
                    Temp=Temp+(L[i][j]*L[k][j])
                L[k][i]=(A[k][i]-Temp)/L[i][i]
                print ("L_"+str(k+1)+str(i+1)+"="+str(L[k][i]))

        for i in range(0,k+1):
            Temp=0
            if(k==i):
                for j in range(0,k):
                    Temp=Temp+(L[k][j]*L[k][j])
                print A[k][k]-Temp
                L[k][k]=sqrt(A[k][k]-Temp)
                print ("L_"+str(k+1)+str(k+1)+"="+str(L[k][k]))
    return L          

def solve_y(b,L):
    y=[]
    for i in range(0,n):
        y.append(0)
    for i in range(0,n):
        temp=0
        for j in range(0,n):
            if(i!=j):
                temp=temp+L[i][j]*y[j]
        y[i]=(b[i]-temp)/L[i][i]
    return y

def solve_x(y,L):
    x=[]
    for i in range(0,n):
        x.append(0)
    for i in range(0,n):
    	m=n-1-i
        temp=0
        for j in range(0,n):
        	k=n-1-j
        	if(m!=k):
				temp=temp+L[k][m]*x[k]
        x[m]=(y[m]-temp)/L[m][m]
    return x


def print_A_L(b,y,x,A,L):
# Printing A,L and b
    print "A is"
    for i in range(0,n):
        for j in range(0,n):
            print (A[i][j]),
        print ''
    print "L is "
    for i in range(0,n):
        for j in range(0,n):
            print (L[i][j]),
        print ''
    print "L' is "   
    for i in range(0,n):
        for j in range(0,n):
            print (L[j][i]),
        print ''
    print "b is "
    for i in range(0,n):
        print b[i]

    print "y is"
    for i in range(0,n):
        print y[i]

    print "x is"
    for i in range(0,n):
        print x[i]
    



b,A,L=input_A()
L=output_L(b,A,L)
y=solve_y(b,L)
x=solve_x(y,L)
print_A_L(b,y,x,A,L)


