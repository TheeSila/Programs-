# Define what 'fizzbuzz' means
# 'F' is a variable that states the max number
def fizzbuzz(F):
    result = []   # Create the output based off of 'F' and the defined number
    for x in range(1, F+1):   # Create the range in terms of 'F' for 'x'
        if x % 7 == 0 and x % 11 == 0:   # If a integer of 7 and 11 print fizzbuzz
            result.append("fizzbuzz")
        elif x % 7 == 0:   # If a integer of 7 print fizz
            result.append("fizz")
        elif x % 11 == 0:   # If a integer of 11 print buzz
            result.append("buzz")
        else:   # If not an integer 7, or 11, or 7 and 11, print the result of initial value
            result.append(str(x))
    return result

# Define what 'main' means
def main():
    print(', '.join(fizzbuzz(100)))   # Print ',' and combine with 'fizzbuzz' while detailing max number (100)

# Print 'main'
main()
