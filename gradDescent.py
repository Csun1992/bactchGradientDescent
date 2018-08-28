import numpy as np
from math import exp

def error(point):
    x = point[0]
    y = point[1]
    return (x*exp(y)-2*y*exp(-x))**2

def gradient(point):
    x = point[0]
    y = point[1]
    xGrad = 2*(exp(y)+2*y*exp(-x))*(x*exp(y)-2*y*exp(-x))
    yGrad = 2*(x*exp(y)-2*exp(-x))*(x*exp(y)-2*y*exp(-x))
    return np.array([xGrad, yGrad])


if __name__ == "__main__":
    learningRate = 0.1
    tolerance = 10**(-14)
    point = np.array([1, 1])
    err = error(point) 
    iteration = 0

    while err > tolerance:
        point = point - learningRate*gradient(point)
        err = error(point)
        iteration += 1 

    print iteration
    print point
