import os
from pyfas import Tpl

def test_init():
    tpl = Tpl("FC1_rev01.tpl")
    assert tpl.fname == "FC1_rev01.tpl"
    assert int(tpl.time[1]) == 60

def test_attributes():
    tpl = Tpl("FC1_rev01.tpl")
    assert tpl._attibutes['CATALOG'] == 331
    assert tpl._attibutes['data_idx'] == 421
    assert 'VOLGB' in tpl.trends[1]

def test_extraction():
    tpl = Tpl("FC1_rev01.tpl")
    tpl.extract(3)
    assert tpl.data[3][0] == 9.973410e6
    assert 'Pressure' in tpl.label[3]

def test_filter():
    tpl = Tpl("FC1_rev01.tpl")
    PTs = tpl.filter_trends('PT')
    assert 'PT' in PTs[3]
    assert 'POSITION' in PTs[3]
    assert 'TIEIN' in PTs[3]
    tpl.trends
    assert 'VOLGB' in tpl.trends[1]

def test_to_excel():
    tpl = Tpl("FC1_rev01.tpl")
    tpl.to_excel()
    assert "data.xlsx" in os.listdir()
    os.remove("data.xlsx")
    tpl.to_excel("test.xlsx")
    assert "test.xlsx" in os.listdir()
    os.remove("test.xlsx")
    tpl.to_excel("home.xlsx", "/tmp")
    assert "home.xlsx" in os.listdir("/tmp")
    os.remove("/tmp/home.xlsx")
