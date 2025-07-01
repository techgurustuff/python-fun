# assignment operators
#+,-,*,/,%,//,**

#Relational operators
# ==,!=,>,<,>=,<=

# logical operators
# and,or,not,in,is,is not

x = 40
y = 50

z = x * y
print('The value of z is', z)

a = x == y # This will be False since 40 is not greater than 50
print('The value of a is', a)
b = x < y  # This will be True since 40 is less than 50
print('The value of b is', b)       
c = x > y  # This will be False since 40 is not greater than 50
print('The value of c is', c)
d = x != y  # This will be True since 40 is not equal to 50
print('The value of d is', d)
e = x >= y  # This will be False since 40 is not greater than or equal to 50
print('The value of e is', e)   
f = x <= y  # This will be True since 40 is less than or equal to 50
print('The value of f is', f)
g = x in [10, 20, 30, 40, 50]  # This will be True since 40 is in the list
print('The value of g is', g)   
h = x not in [10, 20, 30,40, 50]  # This will be False since 40 is not in the list
print('The value of h is', h)   
i = x is y  # This will be False since x and y are not the same object
print('The value of i is', i)
j = x is not y  # This will be True since x and y are not the same object
print('The value of j is', j)
k = x > y and x < 100  # This will be False since x is not greater than y
print('The value of k is', k)
l = x < y or x < 100  # This will be True since x is less than y
print('The value of l is', l)
m = not (x < y)  # This will be False since x is less than y
print('The value of m is', m)


number = int(input('Enter a number: '))

# check if number is greater than 0
if number >= 0:
    print("it is if statement")
    print(f'{number} is a positive number.')
     # inner if statement
    if number == 0:
        print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

    print("it is end of if statement")
elif number < 0:
    print("it is else if statement")
    print(f'{number} is a negative number.')
else:
    print("it is else statement")
    print('The number is zero.')
    


print('A statement outside the if statement.')
