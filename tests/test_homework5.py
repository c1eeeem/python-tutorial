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

    # assert test_file.card_value(['БТ']) == 14
    # assert test_file.card_value(['Б10']) == 10
    # assert test_file.card_value(['Б10', 'БВ', 'БД', 'БК', 'БТ', 'Б9', 'Ч2']) == [10, 11, 12, 13, 14, 9, 2]
    # assert test_file.card_value(['Ч10', 'ЧВ', 'ЧД', 'ЧК', 'ЧТ', 'П3', 'Б8']) == [10, 11, 12, 13, 14, 3, 8]


def test_is_flash_royal():
    assert test_file.is_flash_royal(['Б10', 'БВ', 'БД', 'БК', 'БТ', 'Б9', 'Ч2']) == True
    assert test_file.is_flash_royal(['Ч10', 'ЧВ', 'ЧД', 'ЧК', 'ЧТ', 'П3', 'Б8']) == True
    assert test_file.is_flash_royal(['К10', 'КВ', 'КД', 'КК', 'КТ', 'К7', 'П6']) == True
    assert test_file.is_flash_royal(['П10', 'ПВ', 'ПД', 'ПК', 'ПТ', 'Б5', 'К4']) == True
    assert test_file.is_flash_royal(['Б10', 'БВ', 'БД', 'ЧК', 'БТ', 'П6', 'Б8']) == False
    assert test_file.is_flash_royal(['Б10', 'БВ', 'БД', 'БК', 'Б10', 'Б7', 'Ч3']) == False
    assert test_file.is_flash_royal(['Б7', 'БВ', 'БД', 'БК', 'БТ', 'П5', 'К9']) == False


def test_is_flash():
    assert test_file.is_flash(['Б2', 'Б5', 'Б7', 'Б9', 'БТ']) == True
    assert test_file.is_flash(['Ч3', 'Ч6', 'Ч8', 'ЧД', 'ЧК', 'П5', 'К9']) == True
    assert test_file.is_flash(['Б2', 'Б5', 'Ч7', 'Б9', 'БТ']) == False
    assert test_file.is_flash(['Б2', 'Б5', 'Б7', 'Б9', 'ЧТ']) == False
    assert test_file.is_flash(['Б2', 'Ч5', 'К7', 'П9', 'БТ', 'БК', 'БД']) == False


def test_is_straight():
    assert test_file.is_straight(['П5', 'К5', 'Б9', 'Б9', 'К9', 'Б10', 'БВ']) == False
    assert test_file.is_straight(['П5', 'К6', 'Б9', 'Б9', 'К9', 'Б10', 'БВ']) == False
    assert test_file.is_straight(['П7', 'К8', 'Б9', 'Б9', 'К9', 'Б10', 'БВ']) == True
    assert test_file.is_straight(['П7', 'К8', 'Б9', 'Б10', 'КВ', 'Б10', 'БВ']) == True
    assert test_file.is_straight(['Б3', 'Б6', 'П7', 'К8', 'Б9', 'Б10', 'КВ']) == True
    assert test_file.is_straight(['Б3', 'П7', 'К8', 'Б9', 'К9', 'Б10', 'КВ']) == True


def test_is_quads():
    assert test_file.is_quads(['Б3', 'П7', 'К8', 'ПВ', 'ЧВ', 'БВ', 'КВ']) == True
    assert test_file.is_quads(['Б3', 'Ч3', 'К3', 'П3', 'БТ', 'П7', 'Ч6']) == True
    assert test_file.is_quads(['Б10', 'Ч10', 'К10', 'П10', 'ЧВ', 'К7', 'Б2']) == True
    assert test_file.is_quads(['Б5', 'Ч5', 'К5', 'П5', 'БВ', 'Ч10', 'П7']) == True
    assert test_file.is_quads(['Б8', 'Ч8', 'К8', 'П8', 'БВ', 'К9', 'П5']) == True
    assert test_file.is_quads(['БТ', 'ЧТ', 'КТ', 'ПТ', 'Ч10', 'Б5', 'П7']) == True
    assert test_file.is_quads(['БТ', 'ЧТ', 'КТ', 'К10', 'Ч10', 'Б5', 'П7']) == False
    assert test_file.is_quads(['Б10', 'Ч6', 'КТ', 'К10', 'Ч10', 'Б5', 'П7']) == False
    assert test_file.is_quads(['Б5', 'Ч7', 'К5', 'П5', 'БВ', 'Ч10', 'П7']) == False


def test_is_pair():
    assert test_file.is_pair(['Б3', 'П7', 'К8', 'ПВ', 'ЧВ', 'БВ', 'КВ']) == False
    assert test_file.is_pair(['Б5', 'Ч7', 'К5', 'П5', 'БВ', 'Ч10', 'П7']) == True


test_card_value()
test_is_flash_royal()
test_is_straight()
test_is_quads()
test_is_pair()
