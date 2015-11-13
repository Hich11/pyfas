from pyfas import Tpl

def test_init():
    tpl = Tpl("FC1_rev01.tpl")
    assert tpl.fname == "FC1_rev01.tpl"

def test_attributes():
    tpl = Tpl("FC1_rev01.tpl")
    assert tpl._attibutes['CATALOG'] == 331
    assert tpl._attibutes['data_idx'] == 421

def test_extraction():
    tpl = Tpl("FC1_rev01.tpl")
    time, data, metadata = tpl.extract(3)
    assert int(time[1]) == 60
    assert data[0] == 9.973410e6
    assert 'Pressure' in metadata

