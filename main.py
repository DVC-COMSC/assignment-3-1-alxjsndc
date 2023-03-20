def main():
    ##################################################
    # Comlete your code here
    ##################################################


    import random

# Generate 3 random numbers
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    number3 = random.randint(0,100)
    print(number1, number2, number3)

# Check if number1 is the smallest variable
    if number1 < number2 and number1 < number3:
        print(number1)

# If number1 isn't the smallest, check if number2 is
    elif number2 < number1 and number2 < number3:
        print(number2)

# otherwise, number3 is the smallest.
    else:
        print(number3)
if __name__ == '__main__':
    main()
