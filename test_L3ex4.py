import L3ex4 as L
def test_total_cost_shopping():
    totalcost=46.75
    result=L.total_cost_shopping()
    assert result==totalcost

def test_cost_of_fruit():
    expected=2.4
    result=L.cost_of_fruits('apple',2)
    assert expected==result

    