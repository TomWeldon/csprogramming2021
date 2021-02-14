num1 = int(input('Please enter a positive integer: '))

#if num1 < 1:
#   print('Please enter a positive number')

#else:
print(num1, end=' ')
while num1 > 1:
       
        if (num1 % 2 == 0):
            num1 = num1 / 2
            print(int(num1), end=' ')
        elif(num1 % 2 ==1):
            num1 = (num1 * 3) + 1
            print(int(num1), end=' ')
