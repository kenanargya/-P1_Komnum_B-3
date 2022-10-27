import matplotlib.pyplot as plt
import numpy as np

function = input("Masukkan fungsi : ")
def f(x):
    f = eval(function)
    return f

def midPoint(x1, x2):
   return (x1 + x2) / 2

x1 = float(input('Masukkan x1: ' ))
x2 = float(input('Masukkan x2: ' ))
itr = int(input('Masukkan iterasi:' ))

if(x1 > x2):
    x1, x2 = x2, x1

xP = np.arange(x1, x2, 0.1)
yP = f(xP)

print('========================= Hasil =========================', end='\n')

for x in range(itr):
    print('-------------- Iterasi: ', x+1 , ' --------------', end='\n')
    markNeg = 0
    fx1 = f(x1)
    fx2 = f(x2)

    print('x1: ', '{0:.8g}'.format(x1))
    print('x2: ', '{0:.8g}'.format(x2))
    print('f(x1): ', '{0:.8g}'.format(fx1))
    print('f(x2): ', '{0:.8g}'.format(fx2))

    x3 = midPoint(x2, x1)
    fx3 = f(x3)

    print('midPoint: ', '{0:.8g}'.format(x3))
    print('f(x3): ', '{0:.8g}'.format(fx3), end='\n\n')

    # Pergantian nilai x1 atau x2 berdasarkan tanda hasil f(x3)
    if(((fx2 < 0 or fx1 > 0) and fx3 < 0) or ((fx2 > 0 or fx1 < 0) and fx3 > 0)):
        x2 = x3
    else:
        x1 = x3

print('Jawabannya adalah antara :  ', '{0:.8g}'.format(x1), 'to', '{0:.8g}'.format(x2), end='\n\n')

plt.plot(xP, f(xP), c = "green")
plt.show()
