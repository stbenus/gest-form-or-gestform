from .context import gf

def test_gest():
    assert gf.translate_number(3) == 'Geste'

def test_form():
    assert gf.translate_number(5) == 'Forme'

def test_gestform():
    assert gf.translate_number(15) == 'Gestform'

def test_number():
    assert gf.translate_number(7) == 7
