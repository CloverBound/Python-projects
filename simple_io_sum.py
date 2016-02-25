#here is a simple addint program with inputs


try: 
    #first input
    firstNumber = input("Please enter the first number you want to add: ")
    
    #second number input to add
    secondNumber = input("And now enter the second number you want to add: ")

    #now we convert the strings to integers and sum them
    summedNumber = int(firstNumber) + int(secondNumber)

    #finally, print the sum
    print ("The sum of", firstNumber, "and", secondNumber, "equals", summedNumber)


except ValueError:
        print("Error: one of your entries is not a number!")
