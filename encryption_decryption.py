eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Функция шифрования 
def encryption(text, step):
    result = ''
    for i in text:
        if i in rus_lower_alphabet:
            if rus_lower_alphabet.find(i) + step <= len(rus_lower_alphabet) - 1:
                result +=  rus_lower_alphabet[rus_lower_alphabet.find(i) + step]
            else:
                result += rus_lower_alphabet[-1 * (rus_lower_alphabet.find(i) + step - len(rus_lower_alphabet))]
        elif i in rus_upper_alphabet:
            if rus_upper_alphabet.find(i) + step <= len(rus_upper_alphabet) - 1:
                result +=  rus_upper_alphabet[rus_upper_alphabet.find(i) + step]
            else:
                result += rus_upper_alphabet[-1 * (rus_upper_alphabet.find(i) + step - len(rus_upper_alphabet))]
        else:
            result += i
    return result
