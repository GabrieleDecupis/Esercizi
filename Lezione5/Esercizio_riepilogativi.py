# esercizio 1

def check_access(username: str, password:..., is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        x = "Accesso consentito"
        return x
    else:
        y = "Accesso negato"
        return y
    

# esercizio 2

def countdown(n: int) -> int:
    number: list = []
    for x in range(n + 1):
        number.append(x)
    number = number[::-1]
    for x in number:
        print(x)

# esercizio 3

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    x = "Operazione permessa"
    y = "Operazione negata"
    
    if conditionA == True:
        return x
    elif conditionB == True and conditionC == True:
        return x
    else:
        return y
    

# esercizio 5 

def frequency_dict(elements: list) -> dict:
    dizionario_vuoto: dict = {}
    for x in elements:
        if x not in dizionario_vuoto.keys():
            dizionario_vuoto[x] = 1
        else:
            dizionario_vuoto[x] += 1

    return dizionario_vuoto
                




# esercizio 6

def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
    return False

# esercizio 7

def check_parentheses(expression: str) -> bool:
    counter = 0
    while counter >= 0:
        for x in expression:
            if x == "(":
                counter += 1
            elif x == ")":
                counter -= 1
            if counter < 0:
                return False
        break
    if counter == 0:
        return True
    if counter > 0:
        return False



# esercizio 8

def count_isolated(number: list[int]) -> int:
    counter = 0
    if len(number) > 0:
        for x in range(len(number)-1):
            if number[x] == number[x + 1]:
                continue
            if number[x] != number[x + 1] and number[x] != number[x - 1]:
                counter += 1
        if number[len(number)-1] != number[len(number)-2]:
            counter += 1
    
    return counter


# esercizio 9

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    copy_list = original_set.copy()
    for x in elements_to_remove:
        if x in original_set:
            copy_list.remove(x)
        else:
            continue
    
    return copy_list

# esercizio 10

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = dict1.copy()
    if dict1 == {}:
        dict3 = dict2.copy()
    
    for x,y in dict2.items():
        for k,v in dict1.items():
            if x == k:
                dict3[k] = v + y
            if x not in dict1:
                dict3[x] = y
    return dict3



print(merge_dictionaries({}, {'a': 10, 'b': 20}))
