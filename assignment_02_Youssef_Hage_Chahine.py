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

#num = int(input('enter a number: '))
#print(count_digits(num))


# ex 2:

def findMax(nums):
    
    if len(nums) == 0: # if there is not a list 
        return []
    elif len(nums) == 1: # if there is only one number in the list
        return nums[0]
    # for more than 1 number in the list
    first = nums[0] # the 1st num in the list
    rest = nums[1:] # the other num in the list
    max_rest = findMax(rest) # to find the max value 

    if first > max_rest: 
        return first
    else:
        return max_rest

#list1 = []
#value = int(input('enter how many numbers: '))
#for i in range(value):
#    i = int(input('enter a number: '))
#    list1.append(i)
#
#result = findMax(list1)
#
#print('Max value: ', result)



# ex 3

def count_tags(contents, tags):
    
    if not contents: # in case there is not a html content
        return 0
    
    start_tag = contents.find("<" + tags) # to find the starting tag
    if start_tag == -1: # when using the .find() method, if the character is not fing it reterns -1
        return 0
    
    end_tag = contents.find(">", start_tag) # to find the ending tag
    if end_tag == -1:
        return 0
    return 1 + count_tags(contents[end_tag + 1:], tags) # to count the occurences html tag in the remaing html content 

html = ''' 
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>
'''
#tag_to_count = input('enter the tag: ')
#tag_count = count_tags(html, tag_to_count)
#print(tag_to_count, tag_count)


def count_digits_menu():
    num = int(input("Enter a number: "))
    print("Number of digits:", count_digits(num))

def find_max_menu():
    list1 = []
    value = int(input("Enter how many numbers: "))
    for i in range(value):
        i = int(input("Enter a number: "))
        list1.append(i)
    result = findMax(list1)
    print("Max value:", result)

def count_tags_menu():
    html = ''' 
    <html>
    <head>
    <title>My Website</title>
    </head>
    <body>
    <h1>Welcome to my website!</h1>
    <p>Here you'll find information about me and my hobbies.</p>
    <h2>Hobbies</h2>
    <ul>
    <li>Playing guitar</li>
    <li>Reading books</li>
    <li>Traveling</li>
    <li>Writing cool h1 tags</li>
    </ul>
    </body>
    </html>
    '''
    tag_to_count = input("Enter the tag: ")
    tag_count = count_tags(html, tag_to_count)
    print(tag_to_count, "count:", tag_count)



def displayMenu():
    print("Menu:")
    print("1. Count Digits")
    print("2. Find Max")
    print("3. Count Tags")
    print("4. Exit")

def main():
    displayMenu()
    choice = int(input("please enter your choice here: "))

    while choice != 4:
        if choice == 1:
            count_digits_menu()
        elif choice == 2:
            find_max_menu()
        elif choice == 3:
            count_tags_menu()
        else:
            print("this is an invalid choice ")
        
        print('\n')
        print(' - - - - - - - - ')
        print('\n')
        
        displayMenu()
        choice = int(input("please enter your choice here: "))
    
    print("Thank you for using my program!, you exited")
    
    
main()

