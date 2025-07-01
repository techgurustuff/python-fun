language = ['python', 'Java', 'GO', 'C++', 'JavaScript', 'PHP', 'Ruby', 'Swift', 'Kotlin']
print(language[1])

for lang in language:
    
    if lang == 'GO':
        print('Found GO in the list')
        continue
    print('This is not GO, it is', lang)
   

print('The length of the language list is', len(language))

num1 = 10
if num1 > 0:
    pass # Placeholder for future code execution

print('This is a placeholder for future code execution')

#function to print a message
def print_message():

    print('This is a function to print a message')  
# Call the function
print_message()

# Function to add two numbers
def add_numbers(a,c, b = 3.14):
    sum = a + b
    return sum       


result = add_numbers(5, 10,40)
print('The result of adding 5 and 10 is', result)
result_1 = add_numbers(50,10)
print('The result of adding 50 and the default value is', result_1)


