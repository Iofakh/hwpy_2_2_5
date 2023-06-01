answer = ''


def parity(x):
    if x % 2:
        return ' нечетное число'
    else:
        return ' четное число'


x = int(input('Введите целое число: '))

if x == 0:
    answer = 'нулевое число'

elif x > 0:
    answer += 'положительное'

else:
    answer += 'отрицательное'

print(answer + parity(x))
