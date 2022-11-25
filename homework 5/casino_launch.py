
from casino_logic import bet
from decouple import config

money = int(config("MY_MONEY"))
print(money)
while True:
    if money <= 0:
        print('У вас не осталось денег!')
        break
    answer = input(f'Запустить рулетка? (Да/Нет) баланс:{money}: ')
    if answer == 'Да':
        slot = input(f'Введите слот для ставки (число от 1 до 30): ')
        if slot.isnumeric() and 1 <= int(slot) <= 30:
            amount = input(f'Введите сумму ставки от 1 до {money}: ')
            if slot.isnumeric() and 1 <= int(amount) <= money:
                money += bet(int(slot), int(amount))
            else:
                print('Неправильная сумма ставки')
        else:
            print('Неправильный слот для ставки')
    elif answer == 'Нет':
        if money < 1000:
            print(f'Вы в проигрыше на {1000 - money}')
        elif money > 1000:
            print(f'Вы в выигрыше на {money - 1000}')
        else:
            print('Ничего не изменилось')
    else:
        print('Такой опции нет')