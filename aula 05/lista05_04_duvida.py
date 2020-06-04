import numpy as np
from scipy.special import factorial
x = np.pi/2
exp = np.arange(0,100,2)
a = x**exp
fact = factorial(exp)
termos = a/fact
termos[1::2]= -1*termos[1::2]
cosvalue = termos.sum()

print(cosvalue)
print(np.cos(x))