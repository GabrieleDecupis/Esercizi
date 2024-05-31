# esercizio 1

def blackjack_hand_total(cards: list[int]) -> int: 
    x:int = sum(cards)    
    if x > 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
        return(sum(cards))
    else:
        return(x)


# esercizio 2

def construct_rectangle(area: float) -> list[float]:
    possibilities:list = [] 
    for length in range (1, area+1): 
        width, invalid = divmod(area, length)  
        if invalid == 0: 
            possibilities.append((length, width))
    lista_temp: list = []
    for a in possibilities:
        b = list(a)
        if b[0] >= b[1]:
            lista_temp.append(b)
        else:
            continue   
    temp_1: int =  100000000000000000000
    best_pair: list = None
    for c in lista_temp:
        d = c[0]-c[1]
        if temp_1 > d:
            temp_1 = d
            best_pair = c

    return best_pair

print(construct_rectangle(20))

# esercizio 3

stopwords = ['the', 'And', 'Is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    text_lower = text.lower() #lo rendo tutto minuscolo
    import re
    text_clear = re.sub(r"[^\w\s]","", text_lower ) # levo tutta la punteggiatura devo usare text_clear
    text_clear = text_clear.split() # splitto tutto
    stopwords_lower = [x.lower() for x in stopwords]
    text_clear_2 = []
    for word in text_clear:
        if word not in stopwords_lower:
            text_clear_2.append(word)
    dic: dict = {}
    for w in text_clear_2:
        if w in dic.keys():
            dic[w] = dic[w] + 1
        else:
            dic[w] = 1
    return dic

word_frequency(text, stopwords)

# esercizio 4

print("Esercizio 4\n")

numbers:list = [4,3,2,7,8,2,3,1,]

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    x = 1
    y = len(nums)
    missing_numbers: list = []
    for z in range(x, y + 1):
        if z not in nums:
            missing_numbers.append(z)
        else:
            continue
    return missing_numbers

print(find_disappeared_numbers(numbers))

# esercizio 5 

print("Esercizio 5\n")


def is_subsequence(s: str, t: str) -> bool:
    vuota = []
    for x in t:
        if x in s:
            vuota.append(x)
        else:
            continue
    v= "".join(x for x in vuota)
    if v == s:
        return True
    else:
        return False
        
# esercizio 6

numeri: list = [3, 6, 1, 8, 4, 7]
def even_odd_pattern(nums: list[int]) -> list[int]:
    numeri_pari:list = []
    numeri_dispari:list = []
    for x in numeri:
        if x % 2 == 0:
            numeri_pari.append(x)
        else:
            numeri_dispari.append(x)
    return numeri_pari + numeri_dispari

print(even_odd_pattern(numeri))

# esercizio 7 

print("Esercizio 7\n")

def prime_factors(n: int) -> list[int]:
    x = 2
    factor:list = []
    while x * x <= n:
        if n % x != 0:
            x += 1
        else:
            n = n//x
            factor.append(x)
    if n > 1:
        factor.append(n)
        return factor

print(prime_factors(4))

# esercizio 8

print("Esercizio 8\n")

def third_max(nums: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    # potete utilizzare queste tre variabili di comodo
    #first_max = second_max = third_max = float('-inf')
    v= list(set(nums)) # levo i duplicati
    if len(v) >= 3:
        first_max = max(v)
        v.remove(first_max)
        second_max = max(v)
        v.remove(second_max)
        third_max = max(v)
        return third_max
    else:
        first_max = max(v)
        return first_max
