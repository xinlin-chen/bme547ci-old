from tachycardia.py import is_tachycardic

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
