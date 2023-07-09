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

# ex 2:

def findMax(nums):
    
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return nums[0]
    
    first = nums[0]
    rest = nums[1:]   
    max_rest = findMax(rest)

    if first > max_rest:
        return first
    else:
        return max_rest

list1 = []
value = int(input('enter how many numbers: '))
for i in range(value):
    i = int(input('enter a number: '))
    list1.append(i)

result = findMax(list1)

print('Max value: ', result)

