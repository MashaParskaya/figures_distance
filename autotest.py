import geometry


def test1():
    d = geometry.Dot(1, 2)
    if (d.x == 1 and d.y == 2):
        print("TEST 1 CORRECT")
    else:
        print("TEST 1 WRONG")


def test2():
    d1 = geometry.Dot(1, 2)
    d2 = geometry.Dot(3, 4)
    d = geometry.mass_center([d1, d2])
    if (d.x == 2 and d.y == 3):
        print("TEST 2 CORRECT")
    else:
        print("TEST 2 WRONG")


def test3():
    d1 = geometry.Dot(0, 0)
    d2 = geometry.Dot(3, 4)
    d = geometry.dist(d1, d2)
    if d - 5 < 0.001:
        print("TEST 3 CORRECT")
    else:
        print("TEST 3 WRONG")


def test4():
    d1 = geometry.Dot(0, 0)
    d2 = geometry.Dot(1, 1)
    d3 = geometry.Dot(2, 2)
    f = geometry.not_line([d1, d2, d3])
    if not f:
        print("TEST 4 CORRECT")
    else:
        print("TEST 4 WRONG")


def test5():
    d1 = geometry.Dot(0, 0)
    d2 = geometry.Dot(0, 1)
    d3 = geometry.Dot(1, 0)
    f = geometry.not_line([d1, d2, d3])
    if f:
        print("TEST 5 CORRECT")
    else:
        print("TEST 5 WRONG")


def test6():
    dots = [geometry.Dot(0, 0), geometry.Dot(0, 1), geometry.Dot(1, 0),
            geometry.Dot(1, 1), geometry.Dot(1, 2), geometry.Dot(2, 1)]
    ans, fig1, fig2 = geometry.find_min_dist(dots, 6)
    if ans - 0.4714 < 0.0001:
        print("TEST 6 CORRECT")
    else:
        print("TEST 6 WRONG")


def Autotest():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
