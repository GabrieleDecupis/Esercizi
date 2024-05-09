#1. School Grading System:
#
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average, and a message indicating 
#whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.

# - prima faccio la somma, poi devo dividere per il numero di voti inseriti

def average_score(name_student: str, score: list ) -> str:
    '''
    This part of the function take as input a list of number int. It do the sum and than divide the sum for the number of score
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
    

