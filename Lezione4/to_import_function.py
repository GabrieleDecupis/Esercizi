def media_aritmetica(list_of_number:list) -> int:
# serve per fare la media aritmetica di una serie di numeri in una lista
    if list_of_number == []:
        return 0
    somma = sum(list_of_number)
    media = somma/len(list_of_number)
    return media

