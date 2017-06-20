import numpy as np

ar1 = np.ones((5,4))
ar2 = np.zeros((5,1))
ar2[0] = 1

print ar1
print ar2
print ar1 * ar2

ar1[1,2] = 10
ar1 *= 2
print ar1
print np.sum(ar1)
print np.sum(ar1, 1)
print np.sum(ar1, 0)
