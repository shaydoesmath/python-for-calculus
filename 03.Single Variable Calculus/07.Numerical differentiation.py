#7: Lesson 2 — Numerical differentiation
#Suppose you have a function \(f(x)\), but you don't know its derivative. Can Python estimate it using only function evaluations?
#Yes. We use the forward difference formula
#f'(x)=\frac{f(x+h)-f(x)}{h}
import numpy as np
def numerical_derivative(f, x, h):
    return (f(x + h) - f(x)) / h
def f(x):
    return x**2-2*x+1
x = 2
h = 0.0000000001
approximation = numerical_derivative(f, x, h)
exact = 2*x - 2
print("Numerical derivative:", approximation)
print("Exact derivative:", exact)
print("Absolute error:", abs(approximation - exact))1
