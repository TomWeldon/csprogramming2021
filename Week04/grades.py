# Program or outputting grades
# Author: Tom Weldon G00398828

# Input percentage float to be rounded.696
percentage = round(float(input('Please enter your percentage mark: ')))


if percentage < 0 or percentage > 100:
    print('Please enter a percentage between 0 and 100')

elif percentage < 40:
    print('Fail')
elif percentage < 50:
    print('Pass')
elif percentage < 60:
    print('Merit 1')
elif percentage < 70:
    print('Merit 2')
else:
    print('Distinction')