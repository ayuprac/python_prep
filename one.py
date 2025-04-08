#printing +ve -ve no.
num = 15
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')
    #_____________________________________________

#nested if else
num = 15
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")

#_____________________________________
#using ternary: 
num =15
print("Positive" if num>=0 else "Negative")