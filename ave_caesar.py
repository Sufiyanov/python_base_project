# put your python code here
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encryption(text, step):
    result = ''
    step = len(text)
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


def split_words(text):
    text = text + '|'
    result = ''
    eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range(len(text) - 1):
        if text[i] in eng_alphabet and not text[i + 1] in eng_alphabet:
            result = result + text[i] + '|'
        elif not text[i] in eng_alphabet and text[i + 1] in eng_alphabet:
            result = result + text[i] + '|'
        else:
            result = result + text[i]
    return result.split('|')



text = input()
result = [encryption(i, len(i)) for i in split_words(text)]
print(*result, sep='')
