def ifFibonacci():
    # enter value you want checked
    n = int(input('Enter number you want checked:'))
    a, b, c = 0, 1, 1
    # if the value is 0 or 1 automatically output
    if n == 0 or n == 1:
        print('Number is part of fibonacci series')
    else:
        #update values until we find a match
        while a < n:
            a = b + c
            c = b
            b = a
        if a == n:
            print('Number is part of fibonacci series')
        else:
            print('Number is not part of fibonacci series')


ifFibonacci()
