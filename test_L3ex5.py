import L3ex5 as L
def test_get_employees_by_age_range():
    lower=22
    upper=24
    expected=[{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result=L.get_employees_by_age_range(lower,upper)
    assert expected==result
def test_calculate_average_salary():
    expected=(5+6+5.6+7+6.5+6)*10000/6
    result=L.calculate_average_salary()
    assert result==expected
def test_get_employees_by_dept():
    expected=[
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result=L.get_employees_by_dept("Sales")
    assert result==expected

