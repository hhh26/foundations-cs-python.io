# ex1

def count_digits(n):
    # make the number absolute incase we enter a negative number
    n = abs(n)
    # every number < 10 will be consider 1 
    if n < 10:
        return 1
    # when n // 10 the last didgit will be removed.
    # every time the function is called we take the resulut and sum by 1
    else:
        result  = 1 + count_digits(n // 10)
    return result

num = int(input('enter a number: '))
print(count_digits(num))
