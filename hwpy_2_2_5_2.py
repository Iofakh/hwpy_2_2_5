vowels = ['a', 'e', 'i', 'o']

word = input('Введите слово: ')

vowels_count = 0
consonants_count = 0

for _ in vowels:
    if _ in word:
        count = word.count(_)
        print(f'{_}: {count}')
        vowels_count += count
    else:
        print(f'{_}: False')

consonants_count = len(word) - vowels_count

print(f'Согласных букв: {consonants_count}\n'
      f'Гасных букв: {vowels_count}.')
