import timeit

initialisation='''
import random
A=[]
B=[]
for i in range(size*size):
    A.append(random.randint(0,10000))
    B.append(random.randint(0,10000))
C=[0]*size*size    
'''

naive='''
for i in range(size):
    for j in range(size):
        for k in range(size):
            C[i + j*size] += A[i + k*size] * B[k + j*size]
           
'''
#Von j ist nur jsize abhängig, deswegen sollte diese Schleife ganz außen sein
#Von k ist neben ksize noch der Index c abhängig, weswegen die Schleife als zweite kommt
#Von i ist nun die eigentliche Operation abhängig, deswegen muss sie als letzte ausgeführt werden
optimised='''
for j in range(size):
    jsize=j*size
    for k in range(size):
        ksize=k*size
        c=k + jsize
        for i in range(size):
            C[i + jsize] += A[i + ksize] * B[c]
   '''
   
repeats=10
size=100
t1 = timeit.Timer(naive, initialisation, globals=globals())   
t2 = timeit.Timer(optimised, initialisation, globals=globals())
time1 = min(t1.repeat(repeats, 1))
print("execution time naive:", (time1*1000), "ms")
time2 = min(t2.repeat(repeats, 1))
print("execution time optimised:", (time2*1000), "ms")
print("Faster:",(1-time2/time1)*100,"%")
#Die Komplexität ändert sich nicht, da die Hauptarbeit immer noch in den drei Schleifen steckt   