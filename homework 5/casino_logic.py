import random


def bet(slot, amount):
    slots = list(range(1, 31))
    winning_slot = random.choice(slots)
    if slot == winning_slot:
        print('Вы выиграли')
        return amount * 2
    else:
        print('Вы проиграли')
        return -amount

