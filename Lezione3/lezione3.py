# Gabriele De Cupis
# 22/04/24

# 4-1. Pizzas: 
# Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
# such as I really love pizza!

print("Esercizio 4-1 \n")

favourite_pizza: list = ("Margherita", "Boscaiola", "Diavola")
print(favourite_pizza)
print()
for x in favourite_pizza:
    print(f"I like very much the {x}")
    print(f"I love this type of pizza \n")

print()

# 4-2. Animals: 
# Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. You could print a sentence, 
# such as Any of these animals would make a great pet!

print("Esercizio 4-2 \n")

animals: list = ("Dog", "Cat", "Parot", "Bunny")
for x in animals:
    print(f"I really like {x}, it is very funny!")
print( )
print(f"The {0} and the {1} are the most common pets!")

print( )

# 4-3. Counting to Twenty: 
# Use a for loop to print the numbers from 1 to 20, inclusive.

print("Esercizio 4-3 \n")

for number in range(1, 30):
    print(number)
    if number == 20:
        break

print( )

# 4-4. One Million: 
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

print("Esercizio 4-4\n")

numbers: list = [x for x in range(1, 11)]
for x in numbers:
    print(x)
print()

# 4-5. Summing a Million: 
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your 
# list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.

print("Esercizio 4-5 \n")

numbers: list = [x for x in range(1, 1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print()

# 4-6. Odd Numbers: 
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number.

print("Esercizio 4-6 \n")

odd_numbers: list = [x for x in range(1, 21, 2)]
print(f"{odd_numbers} \n")
for x in odd_numbers:
    print(x)

print()

