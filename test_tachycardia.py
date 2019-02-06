from tachycardia import is_tachycardic


def test_is_tachycardic():
    ans_1 = is_tachycardic('tachycardic')
    exp_1 = True
    assert ans_1 == exp_1


def test_2():
    ans_2 = is_tachycardic('  tachycardic')
    exp_2 = True
    assert ans_2 == exp_2


def test_3():
    ans_3 = is_tachycardic('tachycardic.')
    exp_3 = True
    assert ans_3 == exp_3


def test_4():
    ans_4 = is_tachycardic('tachycardi')
    exp_4 = False
    assert ans_4 == exp_4


def test_5():
    ans_5 = is_tachycardic('TachyCardic  ')
    exp_5 = True
    assert ans_5 == exp_5


def test_6():
    ans_6 = is_tachycardic('TACHYCARDIC')
    exp_6 = True
    assert ans_6 == exp_6


def test_7():
    ans_7 = is_tachycardic(6)
    exp_7 = False
    assert ans_7 == exp_7
