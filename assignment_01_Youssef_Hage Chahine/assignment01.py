# ex-1:

def factorial_num(n):
    if n == 0:
        return 1
    elif n > 0:
        fact = n * factorial_num(n - 1)
        return fact
    else:
        return print('the number is negative repeat')

number = int(input("enter a number: "))
print(factorial_num(number))


# ex-2:

def calDivisors(n):
    divisors = []

    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

num = int(input("enter a number: "))
print(calDivisors(num))


# ex-3:

def reverseString(k):
    return k[::-1]

word = input("enter a word: ")
print(reverseString(word))

# ex-4

def positiveNum():
    num_list = []
    num_list2 = []
    
    n = int(input("how many numbers you want to enter: "))
    
    for num in range(n):
        num = int(input("enter a number: "))
        num_list.append(num)
    print("num list: ", num_list)

    for i in num_list:
        if i % 2 == 0:
            num_list2.append(i)
    
    return num_list2

result = positiveNum()
print('new list: ', result)


# ex-5:


