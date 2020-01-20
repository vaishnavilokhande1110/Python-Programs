#To print Nth number in fibonacci series

a,b = 0,1
n = int(input('N= '))
#print(a,b,end=' ')
if n<=0:
    print('Not accepted')
elif n==1:
    print(a)
else:
    for i in range(2,n):
        c = a + b
        #print(c,end=' ')
        a = b              
        b = c
    print('\n',n,'no in fibonacci series is = ',b)
