# 9-1. Restaurant:
# 
# Make a class called Restaurant. The __init__() method for Restaurant should store two 
# attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces 
# of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"The restaurant name is: {self.restaurant_name} and his cuisine is {self.cuisine_type}, persone servite: {self.number_served}")
    
    def open_restaurant(self):
        import random
        x = random.random()
        if x < 0.5:
            print(f"The restaurant is open!")
        else:
            print(f"The restaurant is close!")
    
    def set_number_served(self, served: int):
        self.number_served = served
    
    def increment_number_served(self, new_number: int):
        self.number_served = self.number_served + new_number
    


ristorante1 = Restaurant("E' passata la moretta", "Romana")
ristorante2 = Restaurant("Goya", "Asiatica")

# ristorante1.describe_restaurant()
# ristorante2.describe_restaurant()
# ristorante1.open_restaurant()
# ristorante2.open_restaurant()
# print(ristorante1.restaurant_name)
# print(ristorante1.cuisine_type)
# print(ristorante2.restaurant_name)
# print(ristorante2.cuisine_type)

# 9-2. Three Restaurants: 
# 
# Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

ristorante1 = Restaurant("E' passata la moretta", "Romana")
ristorante2 = Restaurant("Goya", "Asiatica")
ristorante3 = Restaurant("Il grottino", "Pizzeria Romana")

# ristorante1.describe_restaurant()
# ristorante2.describe_restaurant()
# ristorante3.describe_restaurant()

# 9-3. Users: 
# 
# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes 
# that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, 
# and call both methods for each user.

class User1:
    def __init__(self, first_name: str, last_name: str, age: int = None, city: str = "Not found"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def describe_user(self): 
        print(f"Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}, City: {self.city}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}, nice to see you again!")


# persona1 = User("Gabriele", "De Cupis", 27, 'Rome')
# persona1.describe_user()
# persona2 = User("Angelo", "Locarini", 20, "Sezze")
# persona2.describe_user()
# persona1.greet_user()
        

# 9-4. Number Served: 
# 
# Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then
# change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were 
# served in, say, a day of business. 

# ristorante1.set_number_served(200)
# ristorante1.increment_number_served(50)        
# ristorante1.describe_restaurant()

# 9-5. Login Attempts: 
# 
# Add an attribute called login_attempts to your User class from Exercise 9-3. 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the 
# User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User:
    def __init__(self, first_name: str, last_name: str, age: int = None, city: str = "Not found"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attemps: int = 0

    def describe_user(self): 
        print(f"Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}, City: {self.city}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}, nice to see you again!")

    def increment_login_attempts(self)-> None:
        self.login_attemps += 1
    
    def reset_login_attempt(self)-> None:
        self.login_attemps = 0

    def login_attempt(self)-> int:
        return self.login_attemps

# 9-6. Ice Cream Stand: 
# An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand 
# that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; 
# just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

class IceCreamSteand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0, flavour =  list[str]):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavour = flavour

    def return_flavour(self):
        return self.flavour


# 9-7. Admin: 
# An administrator is a special kind of user. Write a class called Admin that inherits from the User class 
# you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings 
# like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() 
# that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int = None, city: str = None, privilegis: list[str] = None ):
        super().__init__(first_name, last_name, age, city)
        self.privilegis = privilegis

    def show_privilegis(self):
        return self.privilegis

# 9-8. Privileges: 
# Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as 
# described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in 
# the Admin class. Create a new instance of Admin and use your method to show its privileges.

class Privilegis:
    def __init__(self, privilegis: list[str] = None) -> None:
        self.privilegis = privilegis

    def show_privilegis(self):
        return self.privilegis
    

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int = None, city: str = None, privilegis = Privilegis):
        super().__init__(first_name, last_name, age, city)
        self.privilegis = privilegis

    def show_privilegis(self):
        return self.privilegis.privilegis
        # oppure posso fare self.privilegis.show_privilegis()

# 9-9. Battery Upgrade: 
# Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). 
# This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default 
# battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. 
# You should see an increase in the car’s range.

pass

# 9-10. Imported Restaurant: 
# Using your latest Restaurant class, store it in a module. 
# Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s 
# methods to show that the import statement is working properly.

"""

Done

"""
