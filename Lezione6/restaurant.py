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


