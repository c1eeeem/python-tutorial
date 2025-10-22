# def is_safe_bridge(bridge: str):
#    bridge = bridge.strip()
#    return " " not in bridge

# print(is_safe_bridge("####"))     # True
# print(is_safe_bridge("## ####"))  # False
# print(is_safe_bridge("#"))        # True

import random

deck = [
    'Ч2', 'П2', 'К2', 'Б2',
    'Ч3', 'П3', 'К3', 'Б3',
    'Ч4', 'П4', 'К4', 'Б4',
    'Ч5', 'П5', 'К5', 'Б5',
    'Ч6', 'П6', 'К6', 'Б6',
    'Ч7', 'П7', 'К7', 'Б7',
    'Ч8', 'П8', 'К8', 'Б8',
    'Ч9', 'П9', 'К9', 'Б9',
    'Ч10', 'П10', 'К10', 'Б10',
    'ЧВ', 'ПВ', 'КВ', 'БВ',
    'ЧД', 'ПД', 'КД', 'БД',
    'ЧК', 'ПК', 'КК', 'БК',
    'ЧТ', 'ПТ', 'КТ', 'БТ'
]


def card_value(card: str) -> int:  # 'КД' -> 12 'К10' -> 10
    q = {'В': 11,
         'Д': 12,
         'К': 13,
         'Т': 14}

    value = card[1:]
    if value in 'ВДКТ':
        return q[value]

    return int(value)


def is_flash_royal(cards):
    """
    Возвращает True если в списке cards есть комбинация Флеш. False в ином случае.
    :param cards: список карт
    bool :return: Наличие комбинации Флеш в списке cards
    """
    if all(x in cards for x in ['Ч10', 'ЧВ', 'ЧД', 'ЧК', 'ЧТ']):
        return True
    if all(x in cards for x in ['П10', 'ПВ', 'ПД', 'ПК', 'ПТ']):
        return True
    if all(x in cards for x in ['К10', 'КВ', 'КД', 'КК', 'КТ']):
        return True
    if all(x in cards for x in ['Б10', 'БВ', 'БД', 'БК', 'БТ']):
        return True
    return False


def is_straight(cards: list[str]) -> bool:
    values = []
    for card in cards:
        values.append(card_value(card))

    values_no_dublicate = list(set(values))
    if len(values_no_dublicate) < 5:
        return False

    for i in range(len(values_no_dublicate) - 4):
        if values_no_dublicate[i + 4] - values_no_dublicate[i] == 4:
            return True

    return False


def is_flash(cards):
    suits = [x[0] for x in cards]
    return suits.count('Ч') == 5 or suits.count('П') == 5 or suits.count('К') == 5 or suits.count('Б') == 5


def main():
    count_players = 5
    board: list = []
    players: list[list] = [[] for _ in range(count_players)]

    results = {"флеш-рояль": 0,
               'стрит-флеш': 0,
               'каре': 0,
               'фул-фаус': 0,
               'флеш': 0,
               'стрит': 0,
               'тройка': 0,
               "две пары": 0,
               "пара": 0,
               "старшая карта": 0}

    for _ in range(5):
        random_card = random.choice(deck)
        board.append(random_card)
        deck.remove(random_card)

    for player in players:
        for _ in range(2):
            random_card = random.choice(deck)
            player.append(random_card)
            deck.remove(random_card)

    for hand in players:
        l: list[str] = hand + board
        l.sort(key=card_value)
        if is_flash_royal(l):
            print("Флеш-Рояль")

    # достоинство - value
    # масть - suit

    # print(board)
    # print(players)
    # print(deck)


if __name__ == '__main__':
    main()
