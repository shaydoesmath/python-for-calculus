#2 Loops:
#Suppose we want to double every temperature.
temperatures = [20, 25, 30, 35, 40]
for T in temperatures:
    print(2 * T) 
#We can also use range() to repeat something a specified number of times.
for i in range(5):
    print(i)    
#range(5) generates the integers from zero up to, but not including, five.
temperatures = [20, 25, 30, 35, 40]
for i in range(len(temperatures)):
    print(i, temperatures[i])    
