import hw.homework5 as test_file


def test_card_value():
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

    assert test_file.card_value('Ч2') == 2
    assert test_file.card_value('Ч3') == 3
    assert test_file.card_value('Ч4') == 4
    assert test_file.card_value('Ч4') == 4
    assert test_file.card_value('Ч4') == 4
    assert test_file.card_value('Ч4') == 4
    assert test_file.card_value('Ч4') == 4
    assert test_file.card_value('Ч4') == 4




test_card_value()