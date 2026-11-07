#3. Functions
def square(x):
    return x**2
print(square(4))  # 16
#For numerical work, we'll often turn mathematical expressions into functions.
#For example f(x)=x^2+3x+1
def f(x):
    return x**2 + 3*x + 1
print(f(2))  # 11
#Notice that return gives the calculated result back to the part of the program that called the function