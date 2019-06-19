#
# ONLY WORKS ON *NIX SYSTEMS!
#

import time

def fib1(n):
    if n <= 1:
         return n
    return fib1(n-1) + fib1(n-2)

def fib3(n):
    _, f2 = fib3Impl(n)
    return f2

def fib3Impl(n):
    if n == 0: 
        return 1, 0
    else:
       f1, f2 = fib3Impl(n-1)
       return f1 + f2, f1

def fib5(n):
    (f1,f2)=(1,0)
    while n!=0:
        (f1,f2,n) = (f1+f2, f1, n-1)
    return f2

def mul2x2(a, b):
  return [
    a[0]*b[0]+a[1]*b[2],
    a[0]*b[1]+a[1]*b[3],
    a[2]*b[0]+a[3]*b[2],
    a[2]*b[1]+a[3]*b[3]]

def fib6(n):
  m = [1, 0, 0, 1]
  for _ in range(n):
    m = mul2x2(m, [1, 1, 1, 0])
  return m[1]

def fib7(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n % 2 == 0:
    m = [1, 1, 1, 0]
    m = mul2x2(m, m)
    m2 = [1, 0, 0, 1]
    for _ in range(n//2):
      m2 = mul2x2(m2, m)
    return m2[1]
  else:
    m = [1, 1, 1, 0]
    m2 = mul2x2(m, m)
    m3 = [1, 0, 0, 1]
    for _ in range((n-1)//2):
      m3 = mul2x2(m3, m2)
    m3 = mul2x2(m, m3)
    return m3[1]

def fibrun(fib, n): #probiert die zahl für gegebenes N in unter 10 sekunden zu bestimmen
  try:
    t=time.time()+10
    f = fib(n)
    if time.time()>t:
      return False,-1
    if fib==fib7: assert(f==fib5(n))
    return True,f
  except:
    return False,-1

def getN(fib): #sucht das maximale N
  n=20
  b=True
  while b:
    b,f=fibrun(fib,n)
    if b:
      ff=f
      n*=2
  maximum = n
  minimum = n//2
  while maximum != minimum + 1:
    n = minimum + (maximum-minimum)//2
    b,f = fibrun(fib, n)
    if b:
      ff=f
      minimum = n
    else:
      maximum = n
  print(n)
  #print("N={}, f={:.2e}".format(n,ff)) #(sorgt leider für overflow)

getN(fib1) #result:38, dauert sehr schnell sehr viel länger -> exponentiell durch baumrekursion
getN(fib3) #result:994 ->durch die hilfsfunktion, die die ergebnisse der p letzten aufrufe zurückgibt, nur noch linear rekursiv
getN(fib5) #result:1177478, offensichtlich die beste Version, iterativ, verwenden variablen wieder, linear
getN(fib6) #result:322479
getN(fib7) #result:409843, sollte eigentlich die beste Version sein, ist zumindest auch besser als 6, aber komischerweise langsamer als 5
#da fibonaci zahlen integer sind haben sie gar keine dezimalstellen
