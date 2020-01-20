'''
    The program implemented to print series from 1 to n and n to 1
'''
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n,end=' ')
def print_n_to_1(n):
    if n == 0:
        return
    print(n,end=' ')
    print_n_to_1(n-1)
n = int(input('N='))
print(' Series from 1 to',n )
print_1_to_n(n)
print('\n','Series from',n,'to 1')
print_n_to_1(n)