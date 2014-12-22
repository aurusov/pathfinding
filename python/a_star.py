class Map(object):

    class Coordinate(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, coordinate):
            return self.x == coordinate.x and self.y == coordinate.y

        def getLength(self, coordinate):
            return abs(self.x - coordinate.x) + abs(self.y - coordinate.y)

    class Item(Coordinate):
        def __init__(self, x, y, passability):
            self.coordinate = Map.Coordinate(x, y)
            self.passability = passability

    def __init__(self):
        passabilities = [
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [1, -1, -1, -1, -1, -1, -1, -1, -1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1, -1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1, -1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1, -1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1,  1,  1],
            [1,  1,  1, -1,  1,  1,  1,  1,  1,  1],
        ]

        self.__map__ = []
        y = 0;
        for line in passabilities:
            x = 0;
            items = []
            for passability in line:
                items.append(Map.Item(x, y, passability))
                x += 1
            self.__map__.append(items)
            y += 1
        self.widht = len(self.__map__[0])
        self.heidth = len(self.__map__)

    def get_str(self, coordinate_from, coordinate_to, path):
        result = ''
        for line in self.__map__:
            if result:
                result += '\n'
            for item in line:
                if coordinate_from == item.coordinate:
                    result += ' OO'
                elif coordinate_to == item.coordinate:
                    result += ' XX'
                else:
                    path_item_found = None
                    for path_item in path:
                        if path_item == item.coordinate:
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

    class Node(object):
        def __init__(self, parent, map_item):
            self.parent = parent
            self.map_item = map_item
            self.f = 0.0
            self.g = 0.0
            self.h = 0.0
            self.child = []

        def __str__(self):
            return '(%1d,%1d)[%2d]: %f=%f+%f' % (self.map_item.coordinate.x, self.map_item.coordinate.y, self.map_item.passability, self.f, self.h, self.h)

        def generateChildren(self, map):
            children = []
            if self.map_item.coordinate.x + 1 < map.widht:
                item = map.__map__[self.map_item.coordinate.y][self.map_item.coordinate.x+1]
                if item.passability != -1:
                    children.append(Map.Node(self, item))
            if self.map_item.coordinate.x > 0:
                item = map.__map__[self.map_item.coordinate.y][self.map_item.coordinate.x-1]
                if item.passability != -1:
                    children.append(Map.Node(self, item))
            if self.map_item.coordinate.y + 1 < map.heidth:
                item = map.__map__[self.map_item.coordinate.y+1][self.map_item.coordinate.x]
                if item.passability != -1:
                    children.append(Map.Node(self, item))
            if self.map_item.coordinate.y > 0:
                item = map.__map__[self.map_item.coordinate.y-1][self.map_item.coordinate.x]
                if item.passability != -1:
                    children.append(Map.Node(self, item))
            return children

    def calcPath(self, coordinate_from, coordinate_to):

        item_from = self.__map__[coordinate_from.y][coordinate_from.x]
        item_to = self.__map__[coordinate_to.y][coordinate_to.x]

        root = Map.Node(None, item_from)
        root.g = 0.0
        root.h = root.map_item.coordinate.getLength(coordinate_to)
        root.f = root.g + root.h

        open_set = []
        open_set.append(root)
        closed_set = []

        while open_set:
            open_set.sort(key=lambda node: node.f)
            best_node = open_set[0]

            if best_node.map_item.coordinate == coordinate_to:
                path = [best_node.map_item.coordinate]
                node = best_node
                while node.parent:
                    path = [node.parent.map_item.coordinate] + path
                    node = node.parent
                return path

            open_set.remove(best_node)
            closed_set.append(best_node)

            children = best_node.generateChildren(self)
            for child in children:
                if child in closed_set:
                    continue

                child.g = best_node.g + child.map_item.passability
                child.h = child.map_item.coordinate.getLength(coordinate_to)
                child.f = child.g + child.h

                child_from_open_set = None
                for node_from_open_set in open_set:
                    if node_from_open_set.map_item.coordinate == child.map_item.coordinate:
                        child_from_open_set = node_from_open_set
                        break
                if child_from_open_set:
                    if child_from_open_set.g < child.g:
                        continue
                    open_set.remove(child_from_open_set)

                open_set.append(child)

        return []

map = Map()
coordinate_from = Map.Coordinate(2, 3)
coordinate_to = Map.Coordinate(4, 3)
path = map.calcPath(coordinate_from, coordinate_to)
print map.get_str(coordinate_from, coordinate_to, path)