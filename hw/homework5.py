#def is_safe_bridge(bridge: str):
#    bridge = bridge.strip()
#    return " " not in bridge

#print(is_safe_bridge("####"))     # True
#print(is_safe_bridge("## ####"))  # False
#print(is_safe_bridge("#"))        # True

import random

def card_value(card: str):
    pass


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
 
count_players = 5
board = []
players = [[] for _ in range(count_players)]

results = { "флеш-рояль": 0,
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
    l = hand + board
    l.sort(key=card_value)
    print(l)



#print(board)
#print(players)
#print(deck)





