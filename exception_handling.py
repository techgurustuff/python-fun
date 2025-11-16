try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
finally:
    print("Execution completed.")

try:
    result = 7/0
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
    #result = 8 / num
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except:
    print("Not an even number!")
else:
    if num == 0:
        print("Zero is not allowed")
        
    else:
        result = 1 / num
        print("Reciprocal of", num, "is", result)
