class Map(object):

    class Coordinate(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Item(Coordinate):
        def __init__(self, x, y, passability):
            self.coordinate = Map.Coordinate(x, y)
            self.passability = passability

        def __eq__(self, coordinate):
            return self.coordinate.x == coordinate.x and self.coordinate.y == coordinate.y

    def __init__(self):
        passabilities = [
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [1, -1, -1, -1, -1, -1, -1, -1, -1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1, -1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1, -1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1, -1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        ]

        self.__map__ = [[]]
        y = 0;
        for line in passabilities:
            x = 0;
            items = []
            for passability in line:
                items.append(Map.Item(x, y, passability))
                x += 1
            self.__map__.append(items)
            y += 1

    def get_str(self, coordinate_from, coordinate_to, path):
        result = ''
        for line in self.__map__:
            if result:
                result += '\n'
            for item in line:
                if coordinate_from == item:
                    result += ' OO'
                elif coordinate_to == item:
                    result += ' XX'
                else:
                    path_item_found = None
                    for path_item in path:
                        if path_item == item:
                            path_item_found = path_item
                            
                    if path_item_found:
                        result += '  *'
                    elif item.passability == -1:
                        result += ' ##'
                    elif item.passability == 1:
                        result += '  .'
                    else:
                        result += '%3d' % item.passability
        return result

map = Map()
coordinate_from = Map.Coordinate(2, 3)
coordinate_to = Map.Coordinate(9, 1)
path = [
    coordinate_from,
    Map.Coordinate(3, 3),
    Map.Coordinate(4, 3),
    Map.Coordinate(4, 4),
    Map.Coordinate(4, 5),
]
print map.get_str(coordinate_from, coordinate_to, path)
