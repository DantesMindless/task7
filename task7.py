
#
# task1
#
favmovie = 'Favorite movie'


def my_fav_movie(fav_movie):
    print(f'My favorite movie is {fav_movie}')


my_fav_movie(favmovie)

# task2


country = 'Ukraine'
capital = 'Kyiv'


def make_country(country_key, capital_value):
    dict2 = {country_key: capital_value}
    print(dict2[country])


make_country(country, capital)

# task3

num1 = float(input('Type first number '))
op = input('Select operation ')
num2 = float(input('Type second number '))


def calculator(i, x, y):
    if i == '+':
        res = x + y
        return res
    if i == '-':
        res = x - y
        return res
    if i == '/':
        res = x / y
        return res
    if i == '*':
        res = x * y
        return res


print(calculator(op, num1, num2))

#task4
import random

hangman_list = ['trooper', 'fear', 'orchestra', 'piano', 'spider', 'laptop', 'headphones', 'handgun', 'scar',
                'gasoline', 'airplane', 'rifle', 'shotgun', 'highway', 'calculator', 'luggage', 'carbon']
hangman = [
    '-------\n'
    '|     |\n'
    '|     0\n'
    '|    |||\n'
    '|     |\n'
    '|    | |\n'
    'GAME OVER\n',
    '-------\n'
    '|     |\n'
    '|     0\n'
    '|    |||\n'
    '|     |\n'
    '|\n',
    '-------\n'
    '|     |\n'
    '|     0\n'
    '|    |||\n'
    '|\n'
    '|\n',
    '-------\n'
    '|     |\n'
    '|     0\n'
    '|     |\n'
    '|\n'
    '|\n',
    '-------\n'
    '|     |\n'
    '|     0\n'
    '|\n'
    '|\n'
    '|\n',
    '-------\n'
    '|     |\n'
    '|\n'
    '|\n'
    '|\n'
    '|\n',
    '-------\n'
    '|\n'
    '|\n'
    '|\n'
    '|\n'
    '|\n',
    '|\n'
    '|\n'
    '|\n'
    '|\n',
    '|\n',
    ''
]
hangman_word = random.choice(hangman_list)
tried = ['Used letters']
tries = 9
while tries > 0:
    hangman_secret = ''

    for let in hangman_word:
        if let in tried:
            hangman_secret = hangman_secret + let

        else:
            hangman_secret = hangman_secret + '*'
    if hangman_word == hangman_secret:
        print('Good job')
        break
    print(tried)
    print(hangman_secret)
    hangman_guess = input()
    if hangman_guess in tried:
        print('Type another letter')
    elif hangman_guess in hangman_word:
        print("Got it")
        tried.append(hangman_guess)
        print(hangman[tries])
    else:
        print("Not in the word")
        tries -= 1
        tried.append(hangman_guess)
        print(hangman[tries])

