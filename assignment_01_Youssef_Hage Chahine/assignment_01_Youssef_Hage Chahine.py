# ex-1:

def factorial_num(n):
    # base case: fractorial 0 is 1
    if n == 0:
        return 1
    elif n > 0: 
        # calculate factorial for positive numbers
        fact = n * factorial_num(n - 1)
        return fact
    else:
        # retuen error massage if number is negatif
        return print('the number is negative repeat')

number = int(input("enter a number: "))
print(factorial_num(number))


# ex-2:

def calDivisors(n):
    # create an empty list to store the divisors
    divisors = []
    
    # iterate from 1 to n (inclusive)
    for i in range(1, n+1):
        # check if n is divisible by i without any remainder
        if n % i == 0:
            divisors.append(i)
    return divisors

num = int(input("enter a number: "))
print(calDivisors(num))


# ex-3:

def reverseString(k):
    # create an empty string to store the reversed word 
    reverseWord = ""
    
    #iterate over the characters in the input word in reverse order
    for i in range(len(k) -1, -1, -1):
        # append each characters to the reverseWord string
        reverseWord += k[i]
    return reverseWord 

word = input("enter a word: ")
print(reverseString(word))

# ex-4

def positiveNum():
    # create to empty list
    num_list = [] # this list will store how many numbers we want
    num_list2 = [] # this list will store all the positive numbers 
    
    n = int(input("how many numbers you want to enter: "))
    
    # loop to get n numbers from the user 
    for num in range(n):
        num = int(input("enter a number: "))
        num_list.append(num)
    print("num list: ", num_list)
    
    # iterate over the numbers in num_list
    for i in num_list:
        if i % 2 == 0:
            num_list2.append(i)
    
    return num_list2

result = positiveNum()
print('new list: ', result)


# ex-5:

import string

def strong_password():
    # define character sets for lowercase letters, uppercase letters, and special characters
    letter_lower = string.ascii_lowercase 
    letter_upper = string.ascii_uppercase
    special_char = ['#', '?', '!', '$']

    password = input('enter password: ')

    if len(password) < 8: # ckeck if the password is less than 8 characters
        print("password short should be 8 or more")
        return
    # check if the password is at least 8 characters long and if it contains at least one lowercase, one uppercase and one special character
    elif len(password) > 8 and any(char in password for char in letter_lower) and any(char in password for char in letter_upper) and any(char in password for char in special_char):
        print("Strong password")
    else:
        print("Weak password")
    
    return password
strong_password()

