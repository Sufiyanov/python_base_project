from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Количество паролей для генерации')
count_password = int(input())

print('Длину одного пароля')
len_password = int(input())

print('Включать ли цифры 0123456789?')
if input() == 'да':
    chars += digits
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
if input() == 'да':
    chars += uppercase_letters
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
if input() == 'да':
    chars += lowercase_letters
print('Включать ли символы !#$%&*+-=?@^_?')
if input() == 'да':
    chars += punctuation
print('Исключать ли неоднозначные символы il1Lo0O?')
if input() == 'да':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(length, chars):
    return ''.join(sample(chars, length))
    
for i in range(count_password):
    print(generate_password(len_password, chars))
