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

# 4-7. Threes: 
# Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

print("Esercizio 4-7 \n")

multiples_of_3: list = [x for x in range(3, 31, 3)]
print(f"{multiples_of_3} \n")
for x in multiples_of_3:
    print(x)

print()

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube.

print("Eesercizio 4-8 \n")

cubes: list = []
for x in range(1, 11):
    cubes.append(x**3)
print(cubes)

print()

# 4-9. Cube Comprehension: 
# Use a list comprehension to generate a list of the first 10 cubes.

print("Esercizio 4-9 \n")

cubes2: list = [x**3 for x in range(1,11)]
for x in cubes2:
    print(x)

print()

# 4-10. Slices: 
# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

print("Esercizio 4-10 \n")

cubes2: list = [x**3 for x in range(1,21)]
for x in cubes2:
    print(x)
print()
print(f"The first three items in the list are: {cubes2[0:3]}")
print(f"Three items from the midle of the list are: {cubes2[10:13]}")
print(f"the last three items from the list are: {cubes2[-3:]}")

print()

# altro modo per svolgerlo
# print(f"i primi tre numeri sono: ", end='')
# for y in range(0, 3):
#     print(f"{cubes2[y]}" + " ", end='')
# print()
        
# 4-11. My Pizzas, Your Pizzas: 
# Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

print("Esercizio 4-11 \n")

favourite_pizza2: list = ["Margherita", "Boscaiola", "Diavola"]
favourite_pizza2.append("Gricia")
print(favourite_pizza2)
print()
friend_pizzas: list = ["Margherita", "Boscaiola", "Diavola"]
friend_pizzas.append("Amatriciana")
print(friend_pizzas)
print()
for x in favourite_pizza2:
    print(f"My favourite pizza is: {x}")
print()
for y in friend_pizzas:
    print(f"My friend's favourite pizza is {y}")

print()

# 4-12. More Loops: 
# All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.

print("Esercizio 4-12 \n")

favourite_pizza3: list = ["Margherita", "Boscaiola", "Diavola"]
friend_pizzas2: list = ["Quattro formaggi", "Amatriciana", "Gricia"]
for x in favourite_pizza3:
    print(f"{x}")
print()
for y in friend_pizzas2:
    print(f"{y}")

print()

# 5-1. Conditional Tests: 
# Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

print("Esercizio 4-12 \n")

#cars: list = ["Ferrari", "Audi", "Mercedes-Benz", "Fiat", " Volkswagen", "Aston Martin", "Bugatti", "McLaren", "Maserati", "BMW"]
#for x in cars:
#    if x == "Bugatti" or x == "Ferrari" or x == "Maserati":
#        print(f"The car is a {x}, a fantastic car!!!")
#    else:
#        print(f"Your car is a barrow!")

car = "subaru"
print("Is car == 'subaru'? I predict True.")
if car == "subaru":
    print("the resul is true")
else:
    print("the result is false")

car = "Ferrari"
print("Is car == 'subaru'? I predict False.")
if car == "subaru":
    print("The resul is true")
else:
    print(f"The result is false, your car is a {car}")

print()

# 5-2. More Conditional Tests: 
# You don’t have to limit the number of tests you create to 10. 
# If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings OK
# • Tests using the lower() method OK
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to OK
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

print("Esercizio 5-2 \n")

cars: list = ["Ferrari", "Audi", "Mercedes-Benz", "Volkswagen", "Aston Martin", "Bugatti", "McLaren", "Maserati", "BMW"]
my_cars: list = ["Ferrari", "Bugatti", "Mercedes-Benz"]
for x in cars:
    if x in my_cars:
        print(f"Is your car a {x}?")
        print(f"TRUE \n")
    else:
        print(f"Is your car a {x}?")
        print(f"FALSE\n")

my_dream_car: str = "FERRARI"
car2: list = ["ferrari","audi", "bmw"]
print("Is your car a ferrari?")
print(my_dream_car.lower() == car2[0])

print()

number2: list = [12, 67, 98, 100]
number3: list = [11, 67, 100]

for x in number2:
    for y in number3:
        if x == y:
            print(f"Is {x} = or < or > {y}?")
            print(f"Is {x} = {y}?")
            print(f"TRUE\n")
        else:
            print(f"Is {x} = or < or > {y}?")
            print(f"Is {x} = {y}?")
            print(f"FALSE\n")

for x in number2:
    for y in number3:        
        if y == x:
            print(f"{y} is = {x}")
        elif y > x:
            print(f"{y} is > {x}")
        else:
            print(f"{y} is < {x}")
        if y >= x:
            print(f"{y} is >= {x}\n")
        elif y <= x:
            print(f"{y} is <= {x}\n")

print()

