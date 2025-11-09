# def is_safe_bridge(bridge: str):
#    bridge = bridge.strip()
#    return " " not in bridge

# print(is_safe_bridge("####"))     # True
# print(is_safe_bridge("## ####"))  # False
# print(is_safe_bridge("#"))        # True

import random
import collections

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

rank_combinations = {10: "флеш-рояль",
                     9: 'стрит-флеш',
                     8: 'каре',
                     7: 'фул-фаус',
                     6: 'флеш',
                     5: "стрит",
                     4: "тройка",
                     3: "две пары",
                     2: "пара",
                     1: "старшая карта"}


def card_value(card: str) -> int:
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


def is_straight_flush(cards):
    suits = ['Ч', 'П', 'К', 'Б']
    for suit in suits:
        suited_cards = [c for c in cards if c[0] == suit]
        if len(suited_cards) >= 5 and is_straight(suited_cards):
            return True
    return False


def open_river():
    a = []
    for _ in range(5):
        random_card = random.choice(deck)
        a.append(random_card)
        deck.remove(random_card)

    return a


def deal_hands(count_hands):
    hands = [[] for _ in range(count_hands)]
    for hand in hands:
        for _ in range(2):
            random_card = random.choice(deck)
            hand.append(random_card)
            deck.remove(random_card)

    return hands

def is_quads(cards: list[str]): # ['П5', 'К5', 'Б9', 'Б9', 'К9', 'Б10', 'БВ']
    values = []
    for card in cards:
        values.append(card_value(card))

    # for item in collections.Counter(values).values():
    #     if item == 4:
    #         return True
    for value in values:
        if values.count(value) == 4:
            return True
    return False

def is_pair(cards: list[str]):
    values = [card_value(card) for card in cards]
    for v in set(values):
        if values.count(v) == 2:
            return True
    return False


def is_trips(cards: list[str]):
    values = [card_value(card) for card in cards]
    for v in set(values):
        if values.count(v) == 3:
            return True
    return False


def rank_hand(hand, board):
    l: list[str] = hand + board
    l.sort(key=card_value)
    if is_flash_royal(l):
        return 10
    elif is_straight_flush(l):
        return 9
    elif is_quads(l):
        return 8
    elif


def main():
    count_players = 5
    board: list = open_river()
    players: list[list] = deal_hands(count_players)

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

    for hand in players:
        rank = rank_hand(hand, board)
        results[rank_combinations[rank]] += 1

    # достоинство - value
    # масть - suit

    # print(board)
    # print(players)
    # print(deck)


if __name__ == '__main__':
    main()
