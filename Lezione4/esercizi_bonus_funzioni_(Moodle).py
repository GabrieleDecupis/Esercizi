# esercizio 1

def ransom(note: str, magazine: str) -> bool:
    lettere_magazine: list = []
    lettere_note: list = []
    for x in magazine:
        lettere_magazine.append(x)
    for x in note:
        lettere_note.append(x)
    lettere_in_comune: list = []
    conteggio_lettere_magazzine = {uso_lettera: 0 for uso_lettera in magazine}
    for z in lettere_note:
        for y in lettere_magazine:
            if z == y and conteggio_lettere_magazzine[y] < lettere_magazine.count(y):
                lettere_in_comune.append(z)
                conteggio_lettere_magazzine[y] += 1
                break
    stringa_lettere_in_comune: str = "".join(x for x in lettere_in_comune)
    if stringa_lettere_in_comune == note:
        return True
    else:
        return False




# print(ransom("a","b"))
# print(ransom("aa", "ab"))
# print(ransom("aa","aab"))
# print(ransom("tu sei un figo", "bella per te stai zitto. figo di qua e di là"))
# print(ransom("","ciao"))
# print(ransom("tu sei un figo", "bella per te! ne vuoi stare zitto? figo di qua e di là... senza offesa"))

# esercizio 2
    
def to_hex(num: int) -> str:
    stringa_vuota: list = []

    valori_esadecimali: dict = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15, "0":0, "1":1, 
                                "2":2, "3":3 , "4":4, "5":5, "6":6, "7":7, "8":8, "9":9} 
    if num > 0:
        while num > 0:   
            x = num % 16
            for k,v in valori_esadecimali.items(): 
                if x == v:
                    stringa_vuota.append(k)
            num = num//16
        stringa_vuota = stringa_vuota[::-1]
        numero_esadecimale = "".join(x for x in stringa_vuota)
        return numero_esadecimale
        

    else:
        valori_esadecimali_bis: dict = {"0000": '0', "0001": '1', "0010": '2', "0011":'3', "0100": '4', "0101": '5',
                                        "0110": '6', "0111": '7', "1000": '8', "1001": '9', "1010": 'a', "1011": 'b', 
                                        "1100": 'c', "1101": 'd', "1110": 'e', "1111": 'f'} 
        numero_binario: list = []
        num = - num
        while num >= 1:
            x = num % 2
            numero_binario.append(x)
            num = num // 2

        numero_binario = numero_binario[::-1]
            
        while len(numero_binario) < 32:
            numero_binario.insert(0, 0)
        
        complemento_a_due: list =[]
        for x in numero_binario:
            if x == 0:
                complemento_a_due.append(1)
            else:
                complemento_a_due.append(0)

        y = (len(complemento_a_due) - 1)
        if complemento_a_due[y] != 0:
            complemento_a_due[y] = 0
        else:
            complemento_a_due[y] = 1

        numero_bin: list = []
        for x in complemento_a_due:
            numero_bin.append(str(x))
        gruppi = []
        string: str = ""
        for i,bit in enumerate(numero_bin):
            if i % 4 == 0 and i != 0:
                gruppi.append(string)
                string = ""
            string = string[:] + bit
            if i == 31:
                gruppi.append(string)

        num_esa: str = ""
        for x in gruppi:
            for k,v in valori_esadecimali_bis.items():
                if x == k:
                    num_esa += v

        return num_esa

#print(to_hex(26))
#print(to_hex(168989))
    
# esercizio 3

def ugly_number(num: int) -> bool:
    x = 2
    y = 3
    z = 5
    while num > 1:
        if num % x == 0:
            num //=x
        elif num % y == 0:
            num//=y
        elif num % z == 0:
            num//=z
        else:
            return False
    return True

#print(ugly_number(27))

# esercizio 4

def find_lhs(nums: list[int]) -> int:
    freq_map = {}
    max_lenght = 0

    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    for num in freq_map:
        if num + 1 in freq_map:
            max_lenght = max(max_lenght, freq_map[num] + freq_map[num + 1])
    
    return max_lenght
