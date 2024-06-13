# esercizio 1

# Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
# Handle ValueError if the input is negative by returning an informative message.

import math

def safe_sqrt(numero: int) -> float:
    # if numero < 0:
    #     raise Exception(f"Il numero non può essere minore di 0")
    # return math.sqrt(numero)
    try:
        return math.sqrt(numero)
        
    except ValueError:
        print("il numero deve essere > 0")
        return numero

# print(safe_sqrt(-16))


# esercizio 2

# Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria 
# (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
# Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.

class InvalidPasswordError(Exception):
    """ Invalid Password """


def validate_password(password: str) -> str:
    if len(password) < 20:
        raise InvalidPasswordError("La password deve contenere almeno 20 caratteri")
    
    counter = 0
    for x in password:
        if x.isupper():
            counter += 1
            #x.is
    if counter < 3:
        raise InvalidPasswordError("La password deve contenere almeno 3 caratteri maiuscoli")
    
