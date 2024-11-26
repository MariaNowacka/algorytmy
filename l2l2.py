import time, numpy as np, matplotlib.pyplot as plt, random
from scipy.optimize import curve_fit

''' funkcja znajduje rekurencyjnie największy element w podanej sekwecji
    input : S - lista (sekwencja)
    output : element największy '''
def fun_max(S, max=0):
  n=len(S)
  if len(S)==0:
    return max
  else:
    if max>S[0]:
      return fun_max(S[1::],max)
    if max<S[0]:
      max=S[0]
      return fun_max(S[1::],max)
def func(x,a,b):
  return a*x+b

import random
S=random.sample(list(range(0,2000)), 100)
#print(S)
print(fun_max(S))
xs = list(range(0,1000,100))
ys = []
for i in xs:
  start = time.time()
  fun_max(random.sample(list(range(0, 2000)), i))
  end = time.time()
  ys.append(end-start)
popt, pcov = curve_fit(func, xs, ys)
x2 = np.array(xs)
plt.plot(xs,ys,'ro',label="Dane")
plt.plot(x2, func(x2, *popt), label="Hipoteza")
plt.xlabel("Rozmiar")
plt.ylabel("Czas wykonania")
plt.legend(loc='upper left')
plt.title("func_max")
plt.show()