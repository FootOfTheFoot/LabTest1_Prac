import L3ex3 as L
templist=[4,3,5,7,6]
def test_find_min_max():
    expected=[3,7]
    result=L.find_min_max(templist)
    assert expected==result
def test_calc_average():
    expected=5
    result=L.calc_average(templist)
    assert expected==result

def test_calc_median_temperature():
    expected=5
    result=L.calc_median_temperature(templist)
    assert expected==result