min_investment = int(input('Введите минимальную сумму инвестиций '))
mike_cash = int(input('Введите сумму Майкла '))
ivan_cash = int(input('Введите сумму Ивана '))

if (mike_cash >= min_investment) and (ivan_cash >= min_investment):
    print(2)
elif mike_cash >= min_investment:
    print('Mike')
elif ivan_cash >= min_investment:
    print('Ivan')
elif (mike_cash + ivan_cash) >= min_investment:
    print(1)
else:
    print(0)
