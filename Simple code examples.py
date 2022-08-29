# Fibonacci
n = int(input('Nada n '))
a = 1
b = 1
for i in range(n):
    print(a)
    a, b = b, b+a


""" Напишите функцию, которая переводит в верхний регистр первую и четвёртую буквы имени."""


def old_macdonald(name):
    result = ''

    for i, x in enumerate(name):
        if i == 0 or i == 3:
            result += x.upper()
        else:
            result += x
    return result


""" На входе список чисел, вернуть True если массив содержит где-нибудь 3 рядом с 3."""


def has_33(nums):
    for xzb in range(0, len(nums) - 1):
        if nums[xzb] == nums[xzb + 1] == 3:
            return True
    return False


"""Напишите функцию, которая берёт список чисел, и возвращает True, если в списке содержатся числа 0 0 7 в указанном порядке."""


def spy_game(nums):
    newlist = []

    for item in nums:
        if item in (0, 7):
            newlist.append(item)

    if newlist == [0, 0, 7]:
        return True
    else:
        return False


""" Напишите функцию, которая возвращает количество простых чисел, которые меньше или равны указанному числу."""


def count_primes(num):
    if num < 2:
        return 0

    primes = [2]

    x = 3

    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)


"""Напишите функцию Python, которая принимает на вход строку, и вычисляет количество букв в верхнем регистре и в нижнем регистре."""


def up_low(s):
    countbig = 0
    countsmall = 0

    for letter in s:
        if letter == letter.upper() and letter not in ('.', ',', ' ', '?'):
            countbig += 1
        elif letter != letter.upper() and letter not in ('.', ',', ' ', '?'):
            countsmall += 1

    print('No. of Upper case characters : {}, '.format(countbig), 'No. of Lower case Characters : {} '.format(countsmall))


""" Напишите функцию Python, которая проверяет входную строку, является ли эта строка палиндромом или нет."""


def palindrome(s):
    charger = ''

    for letter in s:
        if letter != ' ':
            charger += letter

    if charger == charger[::-1]:
        return True
    else:
        return False


""" Напишите функцию Python, которая проверяет, является ли строка панграммой или нет."""


def ispangram(test_sent):
    kopilka = ''
    for let in test_sent:
        if let != ' ':
            kopilka = kopilka + let

    newlist = list(test_sent)
    nabor = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    for popeditem in newlist:
        if popeditem in alphabet and popeditem not in nabor:
            nabor += popeditem

    if len(nabor) == 26:
        print(True)
    else:
        print(False)


""" FizzBuzz"""
num = range(1, 101)
for id in num:
    if id % 3 == 0 and id % 5 == 0:
        print('FizzBuzz')
    elif id % 5 == 0:
        print('Buzz')
    elif id % 3 == 0:
        print('Fizz')
    else:
        print(id)


"""Реализуйте методы класса Line (линия), который принимает на вход координаты в виде двух кортежей, и возвращает угол 
наклона (slope) и длину (distance) этой линии."""


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
        print(d)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        s = abs(y2 - y1) / abs(x2 - x1)
        print(s)


"""Реализуйте методы класса и определите обьём и площадь поверхности цилиндра."""


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        pi = 3.14
        v = pi * (self.radius ** 2) * self.height
        print(v)

    def surface_area(self):
        pi = 3.14
        s_a = (2 * pi * self.radius) * self.height + 2 * pi * (self.radius ** 2)
        print(s_a)
