import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    a = 60
    b = 20
    output = methods.soma(a, b)
    assert output == 80

def test_sub():
    a = 60
    b = 20
    output = methods.sub(a, b)
    assert output == 40

def test_mult():
    a = 3
    b = 6
    output = methods.mult(a, b)
    assert output == 18

def test_div():
    a = 15
    b = 5
    output = methods.div(a, b)
    assert output == 3


