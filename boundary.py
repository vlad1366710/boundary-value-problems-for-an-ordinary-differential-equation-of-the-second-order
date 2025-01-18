import numpy
A=1.2
B=1.5
alpha=1 
alpha2=0
gamma=1

betha=2
betha2=-1
gamma2=0.5
x=1.2
h=0.05
n=6
y=numpy.zeros(n+1)

def p(x):
    return(3)
def q(x):
    return(-1/x)
def f(x):
    return(x+1)
def prog (A, B, C ,D, N,a):
    # A[0] = 0 
    # C[N - 1] = 0
    p = numpy.zeros(N)
    q = numpy.zeros(N)
    p[0] = -C[0] / B[0]
    q[0] = D[0] / B[0]
    for i in range(1,N):
        q[i] = (D[i] - A[i] * q[i - 1]) / (A[i] * p[i - 1] + B[i])
        p[i] = -C[i] / (A[i] * p[i - 1] + B[i])
       
    result = numpy.zeros(N)
    result[N - 1] = q[N - 1]
    for i in range (N-2,-1,-1):
        result[i] = p[i] * result[i + 1] + q[i]
    for i in range(N):
        print("y(0,",a+i*h,") = ",result[i])
        
    return result

yi1 = numpy.zeros(n+1)
yi= numpy.zeros(n+1)
yi11 = numpy.zeros(n+1)
d = numpy.zeros(n+1)

for i  in range(1,n):
    x = x+h
    yi1[i]= 1+0.5*p(x)*h
    yi[i] = -2+q(x)*h*h
    yi11[i] = 1-0.5*p(x)*h
    d[i] = h*h*f(x)
yi1[0]= alpha2/h
yi[0] = alpha-alpha2/h
yi11[0] = 0
d[0] = gamma

yi1[n]= 0
yi[n] = betha+betha2/h
yi11[n] = -betha2/h
d[n] = gamma2
prog(yi11,yi,yi1,d,n+1,A)
