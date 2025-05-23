import L3ex2 as L
arr=[3,7,2,9,4]
def test_asc():
    expected=[2,3,4,7,9]
    result=L.bubble_sort(arr, L.SORT_ASCENDING)
    assert result==expected

def test_desc():
    expected=[9,7,4,3,2]
    result=L.bubble_sort(arr, L.SORT_DESCENDING)
    assert result==expected

def test_input_normal():
    expected=1
    result=L.bubble_sort(arr, L.SORT_DESCENDING)
    assert result==expected

def test_input_zero():
    testArr=[]
    expected=0
    result=L.bubble_sort(testArr, L.SORT_DESCENDING)
    assert result==expected

def test_input_invalid():
    testArr=[1,"hi"]
    expected=2
    result=L.bubble_sort(testArr, L.SORT_DESCENDING)
    assert result==expected