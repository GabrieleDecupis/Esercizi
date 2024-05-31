# Gabriele De Cupis
# 17/04/24

print("Hello World!! \n")

# 2-3. Personal Message: 
# Use a variable to represent a person’s name, and print a message to that person. 
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

print("Esercizio 2-3 \n")

name: str = "Giuseppe"
message: str = f"ciao {name}, ti va di imparare un po' di phyton insieme?"
print(f"{message}\n")
print(   )

# print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: 
# Use a variable to represent a person’s name, 
# and then print that person’s name in lowercase, uppercase, and title case.

print("Esercizio 2-4 \n")

name2: str = "gAbrIelE"
print(name2)
print(name2.upper())
print(name2.lower())
print(name2.title())

print(      )

# 2-5. Famous Quote: 
# Find a quote from a famous person you admire.
# Print the quote and the name of its author. Your output should look something like the following, 
# including the quotation marks: 
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print("Esercizio 2-5 \n")

quote: str =  "I am the master of my fate, I am the captain of my soul"
print(f"William Ernest Henley once said: \"{quote}\".")

print(      )
# 2-6. Famous Quote 2: 
# Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
# Then compose your message and represent it with a new variable called message. Print your message. 

print("Esercizio 2-6 \n")

famous_person: str = "William Ernest Henley"
print(f"{famous_person} once said: \"{quote}\".")

print(      )

# 2-8. File Extensions: 
# Python has a removesuffix() method that works exactly like removeprefix(). 
# Assign the value 'python_notes.txt' to a variable called filename. 
# Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

print("Esercizio 2-8 \n")

filename: str = "python_notes.txt"
print(filename.removesuffix(".txt"))

print(      )

# 3-1. Names: 
# Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

print("Esercizio 3-1 \n")

names: list = ["Giuseppe","Angelo","Pippo","Pluto",]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(      )

# 3-2. Greetings: 
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.

print("Esercizio 3-2 \n")

print("Ciao", names[0], "come stai?")
print("Ciao", names[1], "come stai?")
print("Ciao", names[2], "come stai?")
print("Ciao", names[3], "come stai?")

print(      )

# 3-3. Your Own List: 
# Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

print("Esercizio 3-3 \n")

mode_of_transportation: list = ["Ferrari 'La Ferrari'","wingsuit","F22 - Raptor"]
print("I would like to do some laps at Mugello with",mode_of_transportation[0])
print("I will be very happy if one day I fly with the",mode_of_transportation[1])
print("I hope that one day I will see a", mode_of_transportation[2])

print(      )

# 3-4. Guest List: 
# If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

print("Esercizio 3-4 \n")

guest_list: list = ['Tony Stark','Nelson Mandela','Yvonne Stravonsky']
print("Hello dear",guest_list[0],"you are invite to my house for a dinner! If you want you can bring your Suits")
print("Mister",guest_list[1],"it's my pleasure invite you to my house for a dinner. I hope you will come, best wishes!")
print("Hello", guest_list[2], "will be form me an honor to have you to my dinner. Let me know if you will come!")

print(      )

# 3-5. Changing Guest List: 
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print("Esercizio 3-5 \n")

print(guest_list[1])
guest_list.pop(1)
guest_list.append('Miriam Leone')
print(guest_list)
print("Hello dear",guest_list[0],"you are invite to my house for a dinner! If you want you can bring your Suits")
print("Miss",guest_list[1],"it's my pleasure to invite you to my house for a dinner. I hope you will come, best wishes!")
print("Hello", guest_list[2], "will be form me an honor to have you to my dinner. Let me know if you will come!")

print(      )

# 3-6. More Guests: 
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. 
# Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

print("Esercizio 3-6 \n")

print(f"Dear {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, I have a new bigger table so I can invite 3 more person! \nDo you have some suggestions?")
guest_list.insert(0, "Scarlett Johansson")
guest_list.insert(2, "Margot Robbie")
guest_list.append("Jennifer Aniston")
print(f"Hello,{guest_list[0]}, will be form me an honor to have you to my dinner. Let me know if you will come!")
print(f"Hello,{guest_list[1]}, will be form me an honor to have you to my dinner. Let me know if you will come!")
print(f"Hello,{guest_list[2]}, will be form me an honor to have you to my dinner. Let me know if you will come!")
print(f"Hello,{guest_list[3]}, will be form me an honor to have you to my dinner. Let me know if you will come!")
print(f"Hello,{guest_list[4]}, will be form me an honor to have you to my dinner. Let me know if you will come!")
print(f"Hello,{guest_list[5]}, will be form me an honor to have you to my dinner. Let me know if you will come!")

print(      )

# 3-7. Shrinking Guest List: 
# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

print("Esercizio 3-7 \n")

print(guest_list)
eliminato1: str = guest_list.pop(1)
print(f"I'm really sorry dear {eliminato1} but my dinner is cancelled")
eliminato2: str = guest_list.pop(4)
print(f"I'm really sorry dear {eliminato2} but my dinner is cancelled")
eliminato3: str = guest_list.pop(1)
print(f"I'm really sorry dear {eliminato3} but my dinner is cancelled")
eliminato4: str = guest_list.pop(1)
print(f"I'm really sorry dear {eliminato4} but my dinner is cancelled")
print(guest_list)
print(f"Dear {guest_list[0]} and {guest_list[1]}, you're still invited to my dinner!")
del(guest_list[1])
del(guest_list[0])
print(guest_list)

print(      )

#3-8. Seeing the World:
# Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list. OK
# Use sorted() to print your list in alphabetical order without modifying the actual list. OK
# Show that your list is still in its original order by printing it. OK
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. OK
# Show that your list is still in its original order by printing it again. OK
# Use reverse()  to change the order of your list. Print the list to show that its order has changed. OK
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

print("Esercizio 3-8 \n")

places: list = ["Islanda", "Svezia", "Norvegia", "Hawaii", "Capo Nord"]
print(places)
print(sorted(places))
print(places)
print(sorted(places)[::-1])
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print(      )

# 3-9. Dinner Guests: 
# Working with one of the programs from Exercises 3, 
# use len() to print a message indicating the number of people you’re inviting to dinner.

print("Esercizio 3-9 \n")

print(len(places))

print(      )

# 3-10. Every Function: 
# Think of things you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

print("Esercizio 3-10 \n")

mountains: list = ["Alpi","Pirenei", "Appennini","Urali","Balcani"]
print(mountains)
mountains.append("Carpazzi")
print(mountains)
mountains.insert(0,"Himalaya")
print(mountains)
print(len(mountains))
mountains.pop(3)
print(mountains)
print(sorted(mountains))
print(mountains)
mountains.reverse()
print(mountains)
mountains.sort()
print(mountains)
del(mountains[0:]) # ha cancellato tutto, altro modo è del(mountains[:7])
print(mountains)

print(  )

# 6-1. Person: 
# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

print("Esercizio 6-1\n")

information: dict = {"First Name": 'Gabriele', "Last Name": 'De Cupis', "Age": 27, "City": 'Rome'}
print(information["First Name"])
print(information["Last Name"])
print(information["Age"])
print(information["City"])

print(          )

# 6-2. Favorite Numbers: 
# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.

print("Esercizio 6-2\n")

favourite_numbers: dict = {"Giuseppe": 17, "Angelo": 98, "Gabriel": 42, "Gioele": 21, "Emanuele": 10}
print(list(favourite_numbers.keys())[0],list(favourite_numbers.values())[0])
print(list(favourite_numbers.keys())[1],list(favourite_numbers.values())[1])
print(list(favourite_numbers.keys())[2],list(favourite_numbers.values())[2])
print(list(favourite_numbers.keys())[3],list(favourite_numbers.values())[3])
print(list(favourite_numbers.keys())[4],list(favourite_numbers.values())[4])

print(      )

# altro modo per svolgere l'esercizio con un ciclo for

for k, v in favourite_numbers.items():
    print(k, v)

print(  )

# 6-3. Glossary: 
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, 
# or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

print("Esercizio 6-3\n")

glossary: dict = {"DEL":"elimina un elemento della lista senza restituire un output", "SORTED":"temporaneamente li mette in ordine alfabetico"}
for k, v in glossary.items():
    print(f"{k} = {v}")

print( )

# 6-7. People: 
# Start with the program you wrote for Exercise 6-1. 
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. 
# As you loop through the list, print everything you know about each person.

print("Esercizio 6-7\n")

information: dict = {"First Name": 'Gabriele', "Last Name": 'De Cupis', "Age": 27, "City": 'Rome'}
information2: dict = {"First Name": 'Giuseppe', "Last Name": 'Guttoriello', "Age": 28, "City": 'Viterbo'}
information3: dict = {"First Name": 'Angelo', "Last Name": 'Locarini', "Age": 19, "City": 'Latina'}
people: list = [information, information2, information3]
for info in people:
    for k,v in info.items():
        print(f"{k} = {v}")
    print("")

print(     )

# 6-8. Pets: 
# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet. 

print("Esercizio 6-8\n")

pet1: dict = {"Owner's name": "Gabriele", "Kind of animal": "Dog", "Name": "Astrid"}
pet2: dict = {"Owner's name": "Pippo", "Kind of animal": "Frog"}
pet3: dict = {"Owner's name": "Paperino", "Kind of animal": "Duck"}
pet4: dict = {"Owner's name": "Topolino", "Kind of animal": "Cat"}
pet5: dict = {"Owner's name": "Pluto", "Kind of animal": "Bird"}
pets: list = [pet1, pet2, pet3, pet4, pet5]
for pet in pets:
    for k,v in pet.items():
        print(f"{k}: {v}")
    print()

print(  )

# 6-9. Favorite Places: 
# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, 
# and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite places.

print("Esercizio 6-9\n")

favourite_places: dict = {'Gabriele':'Islanda, Norvegia', 'Manuela':'Spagna, Irlanda, Portogallo', 'Marcello': 'Bali'}
for k,v in favourite_places.items():
    print(f"{k} loves this places: {v}")

print()

# 6-10. Favorite Numbers: 
# Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

print("Esercizio 6-10 \n")

favourite_numbers2: dict = {"Giuseppe": (17, 55, 60), "Angelo": (98, 89, 12), "Gabriel": (42, 24), 
                            "Gioele": (21, 35), "Emanuele": (10, 75)}
for k,v in favourite_numbers2.items():
    print(f"{k} favourite numbers are: {v}")

print()

# 6-11. Cities: 
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

print("Esercizio 6-11 \n")

cities: dict = {"Rome": [("Italy"), ("5 milion"), ("The capital of the roman Empire")], 
                "New York": [("USA"), ("8 milion"), ("colonized by Amsterdam")],
                "Liverpool": [("England"), ("10 milion"), ("the home town of the Beatles")]}
for k,v in cities.items():
    print(f"{k} is a city in the state of {v[0]}")
    print(f"{k} has {v[1]} abitants!")
    print(f"A fact about {k}: it was {v[2]}")
    print()
print()

# 6-12. Extensions: 
# We’re now working with examples that are complex enough that they can be extended in any number of ways. 
# Use one of the example programs from this chapter, and extend it by adding new keys and values, 
# changing the context of the program, or improving the formatting of the output.

print("Esercizio 6-12 \n")

favourite_numbers3: dict = {"Giuseppe": [(17), (55), (60), (58)], "Angelo": [(98), (89), (12), (90)], 
                            "Gabriel": [(42), (24)], "Gioele": [(21), (35), (86)], 
                            "Emanuele": [(10), (75)]}
for k,v in favourite_numbers3.items():
        for x in range(len(v)):
            print(f"The number that {k} choose is {v[x]}")
        if x == len(v) - 1:
            print(f"{k} don't choose another number!\n")