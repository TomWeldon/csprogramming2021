num1 = int(input('Please enter a positive integer: '))
posInt = num1 > 1
if posInt:
    
    print(num1, end=' ')
    while num1 > 1:

        if (num1 % 2 == 0):
            num1 = num1 / 2
            print(int(num1), end=' ')
        elif(num1 % 2 ==1):
            num1 = (num1 * 3) + 1
            print(int(num1), end=' ')

else:
    print('No positive number entered. Program will exit!')