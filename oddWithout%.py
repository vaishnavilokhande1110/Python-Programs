#program to check number is odd or not without using modulus operator and using bitwise & operator

num = int(input('N='))

if num&1:
    print('ODD')
else:
    print('EVEN')