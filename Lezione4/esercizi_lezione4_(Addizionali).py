#1. School Grading System:
#
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average, and a message indicating 
#whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.

# - prima faccio la somma, poi devo dividere per il numero di voti inseriti

def average_score(name_student: str, score: list[int] ) -> str:
    '''
    This part of the function take as input the name of the student and a list of number int. 
    It do the sum and than divide the sum for the number of score
    '''
    sum_scores = sum(score)
    weighted_average = sum_scores / len(score) #media ponderata

    if weighted_average >= 60:
        print(f"{name_student}, average score:{weighted_average}. PASS\n")
    else:
        print(f"{name_student}, average score:{weighted_average}. FAILED\n")

student_list:list = ["Gabriele", "Alberto", "Aldo", "Giovanni", "Giacomo"]
student_score: list = [[100, 90, 80, 100], [100, 20, 90, 10], [90, 80, 70, 30], [20, 60, 80, 90], [10, 30, 50, 70]]

for x in range(len(student_list)):
    if len(student_list) == len(student_score):
        average_score(student_list[x], student_score[x])
    else:
        print(f"Someone doesn't have their votes recorded")
        break

#2. Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

import random
def guess_the_number():
    first_question: int = int(input("Specify the range you want to play with, from 0 to: "))
    random_number = random.randrange(first_question)
    counter_try = 0
    print()
    print("You have 10 attemps for guess the number!\n")
    while counter_try <= 10:
        x:int = int(input("Insert a number: "))
        print()
        if x > random_number:
            print("Your number is too high!\n")
        elif x < random_number:
            print("Your number is too low!\n")
        else:
            print("CORRECT!! You guess the number!\n")
            break
        counter_try += 1
        y = 10 - counter_try
        print(f"You still have {y} attempts available\n")


# guess_the_number()


# 3. E-commerce Shopping Cart:
# 
# Create a function that defines a product with a name, price, and quantity.
# Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
# The function should calculate the cart total and apply any discounts or taxes.
# Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

def product(name: str, price:float, quantity:int) -> list:
    e_commerce: list = []
    product:dict = {}
    if name not in product:
        product["Name"] = name
    if price not in product:
        product["Price"] = price
    if quantity not in product:
        product["Quantity"] = quantity
    
    e_commerce.append(product)
    return e_commerce

# 4. Text Analysis:
# 
# Create a function that reads a text file and counts the number of occurrences of each word.
# The function should print a report showing the most frequent words and their number of occurrences.
# You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
# Implement error handling to handle missing files or other input issues.

def text_analysis(text:str) -> dict:
    import string
    word_count: dict = {}
    text = text.split()
    parole_senza_punteggiatura = [''.join(parola for parola in parola if parola not in string.punctuation) for parola in text]
    for x in parole_senza_punteggiatura:
        if x not in  word_count:
            word_count[x] = 1
        elif x in word_count:
            word_count[x] += 1
    
    v = list(word_count.values())
    k = list(word_count.keys())
    most_frequent_word = {k[v.index(max(v))] : max(v)}
    
    return most_frequent_word