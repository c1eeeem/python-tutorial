import hw.homework5 as test_file


def test_card_value():
    # 2
    assert test_file.card_value('Ч2') == 2
    assert test_file.card_value('П2') == 2
    assert test_file.card_value('К2') == 2
    assert test_file.card_value('Б2') == 2

    # тройки
    assert test_file.card_value('Ч3') == 3
    assert test_file.card_value('П3') == 3
    assert test_file.card_value('К3') == 3
    assert test_file.card_value('Б3') == 3

    # четверки
    assert test_file.card_value('Ч4') == 4
    assert test_file.card_value('П4') == 4
    assert test_file.card_value('К4') == 4
    assert test_file.card_value('Б4') == 4

    # 5
    assert test_file.card_value('Ч5') == 5
    assert test_file.card_value('П5') == 5
    assert test_file.card_value('К5') == 5
    assert test_file.card_value('Б5') == 5

    # 6
    assert test_file.card_value('Ч6') == 6
    assert test_file.card_value('П6') == 6
    assert test_file.card_value('К6') == 6
    assert test_file.card_value('Б6') == 6

    # 7
    assert test_file.card_value('Ч7') == 7
    assert test_file.card_value('П7') == 7
    assert test_file.card_value('К7') == 7
    assert test_file.card_value('Б7') == 7

    # 8
    assert test_file.card_value('Ч8') == 8
    assert test_file.card_value('П8') == 8
    assert test_file.card_value('К8') == 8
    assert test_file.card_value('Б8') == 8

    # 9
    assert test_file.card_value('Ч9') == 9
    assert test_file.card_value('П9') == 9
    assert test_file.card_value('К9') == 9
    assert test_file.card_value('Б9') == 9

    # 10
    assert test_file.card_value('Ч10') == 10
    assert test_file.card_value('П10') == 10
    assert test_file.card_value('К10') == 10
    assert test_file.card_value('Б10') == 10

    # валет
    assert test_file.card_value('ЧВ') == 11
    assert test_file.card_value('ПВ') == 11
    assert test_file.card_value('КВ') == 11
    assert test_file.card_value('БВ') == 11

    # дама
    assert test_file.card_value('ЧД') == 12
    assert test_file.card_value('ПД') == 12
    assert test_file.card_value('КД') == 12
    assert test_file.card_value('БД') == 12

    # король
    assert test_file.card_value('ЧК') == 13
    assert test_file.card_value('ПК') == 13
    assert test_file.card_value('КК') == 13
    assert test_file.card_value('БК') == 13

    # туз
    assert test_file.card_value('ЧТ') == 14
    assert test_file.card_value('ПТ') == 14
    assert test_file.card_value('КТ') == 14
    assert test_file.card_value('БТ') == 14


def test_is_flash_royal():
    assert test_file.is_flash_royal(['Б10', 'БВ', 'БД', 'БК', 'БТ']) == True
    assert test_file.is_flash_royal(['Ч10', 'ЧВ', 'ЧД', 'ЧК', 'ЧТ']) == True
    assert test_file.is_flash_royal(['К10', 'КВ', 'КД', 'КК', 'КТ']) == True
    assert test_file.is_flash_royal(['П10', 'ПВ', 'ПД', 'ПК', 'ПТ']) == True

    assert test_file.is_flash_royal(['Б10', 'БВ', 'БД', 'ЧК', 'БТ']) == False
    assert test_file.is_flash_royal(['Б10', 'БВ', 'БД', 'БК', 'Б10']) == False
    assert test_file.is_flash_royal(['Б7', 'БВ', 'БД', 'БК', 'БТ']) == False


def test_is_flash():
    pass

test_card_value()
test_is_flash_royal()
