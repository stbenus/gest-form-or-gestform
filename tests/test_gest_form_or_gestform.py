from .context import gest_form_or_gestform as gf

def test_gest():
    assert gf.number_to_gestform_format(3) == 'Geste'

def test_form():
    assert gf.number_to_gestform_format(5) == 'Forme'

def test_gestform():
    assert gf.number_to_gestform_format(15) == 'Gestform'

def test_number():
    assert gf.number_to_gestform_format(7) == 7
