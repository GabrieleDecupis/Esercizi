# 1.
# 
# Write a function to find all numbers divisible by 7, not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers should be stored in a list and returned as output.

def numeri(num_1: int, num_2: int) -> list[int]:
    numeri_belli: list = []
    for x in range(num_1, num_2 + 1):
        if x % 7 == 0 and x % 5 != 0:
            numeri_belli.append(x)
        else:
            continue

    return numeri_belli

#print(numeri(2000, 3200))

# 2.
# 
# Write a function to calculate the factorial of a number given as input. The number should be returned as output. For example:
# 
#     Input: 8
#     Output: 40320

def factoriale(num: int) -> int:
    num_temp = num
    for x in range(1, num):
        num_temp *= x
    
    return num_temp

#print(factoriale(8))

# 3.
# 
# Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. 
# The list is given as input to the function. All factorials should be returned as output. For example:
# 
#     Input: [2, 5, 8, 10]
#     Output: [2, 120, 40320, 3628800]

def factorial_2(numeri: list[int]) -> list[int]:
    numeri_finali: list = []
    for numero in numeri:
        y = numero
        for x in range(1, numero):
            y *= x
        numeri_finali.append(y)
    return numeri_finali
#print(factorial_2([2, 5, 8, 10]))

# oppure

lista = [2, 5, 8, 10]
lista_vuota = []
for x in lista:
    lista_vuota.append(factoriale(x))

#print(lista_vuota)


# 4.
#
# Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) 
# pairs such that i is an integer between 1 and n (both included). The function should return the dictionary as output. For example:
#
#     Input: 8
#     Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def fun_4(num: int) -> dict:
    numeri: dict = {}
    for x in range(1, num + 1):
        numeri[x] = x*x
    return numeri

#print(fun_4(8))


# 5.
# 
# Write a function that accepts a string with a comma-separated sequence of words as input and prints the words as a 
# comma-separated sequence after sorting them alphabetically. For example:
# 
#     Input: without,hello,bag,world
#     Output: bag,hello,without,world

def ordine_alfabetico(parole: str) -> str:
    x:list = parole.split(",")
    x.sort()
    x = ",".join(x)
    return x

#print(ordine_alfabetico("without,hello,bag,world"))

# 6.
# 
# Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising 
# all sentence characters. For example:
# 
#     Input: Practice makes perfect
#     Output: PRACTICE MAKES PERFECT

def upper(word:str) -> str:
    word = word.upper()
    return word

#print(upper("Practice makes perfect"))


# 7.
# 
# Write a function accepting an input string defined with whitespace-separated words and returning it after 
# removing all duplicates and sorting each word alphanumerically. For example:
# 
#     Input: hello world and practice makes perfect and hello world again
#     Output: again and hello makes perfect practice world


