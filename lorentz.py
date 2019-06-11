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
def xprime(lorentz, beta, x):
    return np.multiply(lorentz, np.subtract(one, np.multiply(beta, x)))

beta = np.array([0.99999, 0.95])
x = np.array([1, 1])
ct = np.array([1, 1])
print(xprime(lorentz(beta, x, ct), beta, x))

