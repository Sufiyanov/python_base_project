from random import *
word_list = ['лев', 'тигр', 'медведь', 'жесть']


def get_word():
    return choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tries]


def check_word(text):
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i in text:
        if not i in rus_upper_alphabet:
            print('Не верный символ')
            return False
    return True


def play(word):
    # тело функции
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    index_word = [i for i in range(len(word))]
    word_completion = list(word_completion)

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))

    while True:
        if not '_' in word_completion:
            print(*word_completion)
            print('Поздравляем, вы угадали слово! Вы победили!')
            break
        elif tries == 0:
            print('загаданное слово -', word)
            print('Вы проиграли')
            break

        print(*word_completion)
        print('Введите букву или слово')
        text = input().upper()
        if check_word(text):
            #
            if len(text) == len(word):
                if text == word:
                    word_completion = text
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    break
                else:
                    tries -= 1
                    print(display_hangman(tries))
                    continue
            elif len(text) == 1:
                for i in index_word:
                    if text == word[i]:
                        word_completion[i] = text
                        index_word.remove(i)
                        #print(word_completion)
                        break
                tries -= 1
                print(display_hangman(tries))
                continue
            else:
                tries -= 1
                print(display_hangman(tries))
                continue


play(get_word())
