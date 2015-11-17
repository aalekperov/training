__author__ = 'Korzhukova'


def areaofroom(x, y):

    """
    :param x: length of a romm
    :param y: width of a room
    :return: area of a room
    """
    _area = x*y
    return _area


def printarea(x,y):
    print("Area of a room is " + str(areaofroom(x,y)))

printarea(87, 57)