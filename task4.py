# Напишите функцию, которая будет определять палиндром ли введенная
# строка. Если да, то напечатать “True”, если нет -“False”.


def check_word():

    word = input('Please write below the word: ')
    if word == word[::-1]:
        return 'True'
    else:
        return 'False'

print(check_word())
