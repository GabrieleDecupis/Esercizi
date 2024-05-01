# Gabriele De Cupis
'''
# 8-1. Message: 
# Write a function called display_message() that prints one sentence telling everyone what you are 
# learning about in this chapter. Call the function, and make sure the message displays correctly.

print("Esercizio 8-1\n")

def display_message():
    print("In this chapter I'm learning how to use the function in python")

display_message()

print()

# 8-2. Favorite Book: 
# Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
# Call the function, making sure to include a book title as an argument in the function call.

print("Esercizio 8-2\n")

def favorite_book(title: str):
    print(f"One of my favorite books is {title}")

favorite_book("Eragon")

print()
 
# 8-3. T-Shirt: 
# Write a function called make_shirt() that accepts a size and 
# the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

print("Esercizio 8-3\n")

def make_shirt(size: str, message: str):
    print(f"You choose a {size} size and your message is '{message}'")

make_shirt("XL", "Hello World!")
make_shirt(size = "L", message = "Hello Universe!")

# Variante

def make_shirt_2():
    size: str = input("Please, choose your size: ")
    message: str = input("Please, choose your message: ")
    print(f"You choose a {size} size and your message is '{message}'")

print()

# 8-4. Large Shirts: 
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

print("Esercizio 8-4\n")

def make_shirt_3(size: str = "L", message: str = "I love Python"):
    print(f"You choose a {size} size and your message is '{message}'")    

make_shirt_3()
make_shirt_3("M", "GooddeMorninghe!")

print()

# 8-5. Cities: 
# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value. Call your function for three different cities, 
# at least one of which is not in the default country.

print("Esercizio 8-5\n")

def describe_city(name_of_the_city: str, name_of_the_country: str = "Italy"):
    print(f"{name_of_the_city} is in {name_of_the_country}")

describe_city("Rome")
describe_city("Florence")
describe_city("New York", "USA")

print()

# 8-6. City Names: 
# Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile". 
# Call your function with at least three city-country pairs, and print the values that are returned.

print("Esercizio 8-6\n")

def city_country(city: str, country: str) -> str:
    message: str = (f"\"{city}, {country}\".")
    return message 

print(city_country("Rome", "Italy"))
print(city_country("Berlin", "Germany"))
print(city_country("Oslo", "Norway"))

print()

# 8-7. Album: 
# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary 
# containing these two pieces of information. Use the function to make three dictionaries 
# representing different albums. 
# Print each return value to show that the  dictionaries are storing the album information correctly. 
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.

print("Esercizio 8-7\n")

def make_album(artist_name: str, album_title: str, songs_number: int = None) -> dict:
    music_album: dict = {}
    if songs_number is None:
        music_album = {"artist name": artist_name, "album title": album_title}
    else:
        music_album = {"artist name": artist_name, "album title": album_title, "songs number": songs_number}
    return music_album

print(make_album("Pink Floyd", "The Wall"))
print(make_album("ACDC", "Back in Black"))
print(make_album("Adele", "21", 11))

print()

# 8-8. User Albums: 
# Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input 
# and print the dictionary that’s created. Be sure to include a quit value in the while loop.

print("Esercizio 8-8\n")

while True:
    x:str = input("Choose an artist: ")  
    y:str = input("Choose an artist's album: ")
    z:str = input("Number of the album's song (press enter if unknown): ")
    print()
    if z != "":
        print(make_album(x, y, int(z)), "\n")
    else:
        print(make_album(x, y),"\n")
    go_on:str = input("Do you want to continue? [S/N]: ")
    if go_on.lower() == "n":
        break
    else:
        print()

print()

# 8-9. Messages: 
# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

print("Esercizio 8-9\n")

def show_messages(list_of_messages: list) -> str:
    print(f"{list_of_messages}\n")
    for x in list_of_messages:
        print(f"{x}\n")

Short_Messages: list = ["Hello world", "Veni, vidi, vici", "I have a dream", "Little message"]
show_messages(Short_Messages)

print()

# 8-10. Sending Messages: 
# Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and moves each 
# message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

print("Esercizio 8-10\n")

def send_messages(list_of_messages_to_send: list) -> list:
    sent_messages: list = []
    for x in list_of_messages_to_send:
        sent_messages.append(x)
    return (sent_messages)

messages_1: list = ["Hello world", "Veni, vidi, vici", "I have a dream", "Little message"]
print(send_messages(messages_1))

print()

# 8-11. Archived Messages: 
# Start with your work from Exercise 8-10. Call the function send_messages() 
# with a copy of the list of messages. After calling the function, 
# print both of your lists to show that the original list has retained its messages.

print("Esercizio 8-11\n")

messages_to_send: list = ["Peace and love", "We want you", "Who you gonna call?", "Ghostbusters!"]
message_sent_1: list = send_messages(messages_to_send)
message_sent_2: list = send_messages(message_sent_1)
print(f"Message to send:{messages_to_send}\n")
print(f"First copy of message sent: {message_sent_1}\n")
print(f"Second copy of message sent: {message_sent_2}\n")

# 8-12. Sandwiches: 
# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

print("Esercizio 8-12\n")

def make_a_sandwich(*ingredients):
    sandwich: list = ingredients
    print(f"Your sandwich will have: {sandwich}")

make_a_sandwich("tonno","pomodoro","insalata")
make_a_sandwich("prosciutto", "mozzarella")
make_a_sandwich("tonno", "uova", "maionese")


# versione più interattiva del programma


def make_a_sandwich_2()->list:
    sandwich_ingredients:list = []
    while True:
        ingredient_temp:str = input("Choose ingredient you want in your sandwich: ")
        if ingredient_temp != "":
            ingredient = ingredient_temp.lower()
            sandwich_ingredients.append(ingredient)
        control:str = input("Do you want tu put something else?[Y/N]: ")
        if control.lower() == "n":
            break    
        else:
            print(f"You choose until now:{sandwich_ingredients}\n")
    print(f"\nYour sandwich will have these ingredients: {sandwich_ingredients}\n")
    while True:
        x: str = input("\nDo you want to remove something?[Y/N]: ")
        if x.lower() == "y":
            print(f"\n{sandwich_ingredients}\n")
            ingredients_to_remove_temp: str = input("Which one do you want to remove?: ")
            ingredients_to_remove = ingredients_to_remove_temp.lower()
            sandwich_ingredients.remove(ingredients_to_remove)
        else:
            break
    print(f"\nYour sandwich will have these ingredients: {sandwich_ingredients}")

make_a_sandwich_2()
'''

# 8-13. User Profile:  
# Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you. 
# All the values must be passed to the function as parameters. 
# The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

print("Esercizio 8-13\n")

def build_profile(name:str, surname:str, age:int, color_hair:str, country:str ) -> str:
    print(f"{name} {surname}, {age} years old, {color_hair} hair and he come from {country}")
    
build_profile("Gabriele", "De Cupis", "27", "black", "Italy")

print()

# 8-14. Cars: 
# Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, 
# such as a color or an optional feature. 
# Your function should work for a call like this one: 
# car = make_car('subaru', 'outback', color='blue', tow_package=True) 
# Print the dictionary that’s returned to make sure all the information was stored correctly. 

print("Esercizio 8-14\n")

def make_car(manufacturer: str, model: str, **kwargs: dict) -> dict:
    car_info = {'manufacturer': manufacturer, 'model of the car': model}
    car_info.update(kwargs)
    return car_info

ferrari = make_car('Ferrari', 'Purosangue', color = 'red', traction = 'four-wheel', HP = 725)
print(ferrari)

# 8-15. Printing Models: 
# Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

print("Esercizio 8-15\n")

from to_import_function import media_aritmetica
numeri: list = [1,2,3,4,5,6,7,8,9]
print(media_aritmetica(numeri))

print()

# 8-16. Imports:
# Using a program you wrote that has one function in it, store that function in a separate file. 
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

print("Esercizio 8-16\n")

list_of_number: list = [10,11,12,13,14,15,16,17]

# mode 1

import to_import_function as to_import_function
print(to_import_function.media_aritmetica(list_of_number))
print()

# mode 2

from to_import_function import media_aritmetica
print(media_aritmetica(list_of_number))
print()

# mode 3

from to_import_function import media_aritmetica as media
print(media(list_of_number))
print()
# in questo modo sto importando la funzione rinominandola, in questo caso l'ho rinominata "media"

# mode 4

import to_import_function as funzioni
print(funzioni.media_aritmetica(list_of_number))
# in questo caso invece ho importato il file con un nuovo nome, ovvero "funzioni"
print()

# mode 5

from to_import_function import *
print(media_aritmetica(list_of_number))
# in questo caso importo tutte le funzioni presenti nel file

print()

#8-17. Styling Functions: 
#Choose any three programs you wrote for this chapter, and make sure they follow the 
#styling guidelines described in this section.

print("Esercizio 8-17\n")
print("Done")
 
