import L3ex1 as L
def test_bmi_normal_weight():
    result=L.calculate_bmi(weight=57, height=1.73)
    expected=0
    assert expected==result

def test_bmi_over_weight():
    result=L.calculate_bmi(weight=90, height=1.73)
    expected=1
    assert expected==result

def test_bmi_under_weight():
    result=L.calculate_bmi(weight=30, height=1.73)
    expected=-1
    assert expected==result