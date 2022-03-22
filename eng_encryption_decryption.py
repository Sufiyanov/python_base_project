eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Функция шифрования
def encryption(text, step):
    result = ''
    for i in text:
        if i in eng_lower_alphabet:
            if eng_lower_alphabet.find(i) + step <= len(eng_lower_alphabet) - 1:
                result +=  eng_lower_alphabet[eng_lower_alphabet.find(i) + step]
            else:
                result += eng_lower_alphabet[(eng_lower_alphabet.find(i) + step - len(eng_lower_alphabet))]
        elif i in eng_upper_alphabet:
            if eng_upper_alphabet.find(i) + step <= len(eng_upper_alphabet) - 1:
                result +=  eng_upper_alphabet[eng_upper_alphabet.find(i) + step]
            else:
                result += eng_upper_alphabet[(eng_upper_alphabet.find(i) + step - len(eng_upper_alphabet))]
        else:
            result += i
    return result


# Функция расшифрования
def decryption(text, step):
    result = ''
    for i in text:
        if i in eng_lower_alphabet:
            if eng_lower_alphabet.find(i) - step >= 0:
                result +=  eng_lower_alphabet[eng_lower_alphabet.find(i) - step]
            else:
                result += eng_lower_alphabet[(eng_lower_alphabet.find(i) - step + len(eng_lower_alphabet))]
        elif i in eng_upper_alphabet:
            if eng_upper_alphabet.find(i) - step >= 0:
                result +=  eng_upper_alphabet[eng_upper_alphabet.find(i) - step]
            else:
                result += eng_upper_alphabet[(eng_upper_alphabet.find(i) - step + len(eng_upper_alphabet))]
        else:
            result += i
    return result

text = 'to be, or not to be, that is the question!'
text1 = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'

print(encryption(text, 17))

print(decryption(text1, 25))
