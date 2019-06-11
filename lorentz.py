import numpy as np

one = np.array([1])

# assume beta is the fraction of the speed of light
# the other reference frame is traveling at
#
# e.g v=0.999c beta=0.999
# x and t are in spacetime meters
def lorentz(beta, x, ct):
    return np.divide(one, np.sqrt(np.subtract(one, np.power(beta, 2))))

# result in spacetime meters
def xprime(lorentz, beta, x, ct):
    return np.multiply(lorentz, np.subtract(x, np.multiply(beta, ct)))

def ctprime(lorentz, beta, x, ct):
    return np.multiply(lorentz, np.subtract(ct, np.multiply(beta, x)))

beta = np.array([0.99999, 0.99999])
x = np.array([1, 2])
ct = np.array([1, 2])
lor = lorentz(beta, x, ct)
xpr = xprime(lor, beta, x, ct)
ctpr = ctprime(lor, beta, x, ct)

print(xpr)
print(ctpr)
