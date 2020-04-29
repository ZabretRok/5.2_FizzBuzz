print ("Hello and welcome to the FizzBuzz game! ")

number = int(input("Please, enter a number, between 1 and 100: "))

for num in range (1, number +1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(num)