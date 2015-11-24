class Map(object):

    class Coordinate(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(point1, point2):
            return point1.x == point2.x and point1.y == point2.y

        def getLength(point1, point2):
            return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    class Item(Coordinate):
        def __init__(self, x, y, passability):
            self.coordinate = Map.Coordinate(x, y)
            self.passability = passability

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
                            break

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
        def __init__(self, parent, coordinate):
            self.parent = parent
            self.coordinate = coordinate
            self.f = 0.0
            self.g = 0.0
            self.h = 0.0

        def __eq__(node1, node2):
            return node1.coordinate == node2.coordinate

        def generateChildren(node, map):
            children = []
            if node.coordinate.x + 1 < map.widht:
                item = map.__map__[node.coordinate.y][node.coordinate.x+1]
                if item.passability != -1:
                    children.append(Map.Node(node, item.coordinate))
            if node.coordinate.x > 0:
                item = map.__map__[node.coordinate.y][node.coordinate.x-1]
                if item.passability != -1:
                    children.append(Map.Node(node, item.coordinate))
            if node.coordinate.y + 1 < map.heidth:
                item = map.__map__[node.coordinate.y+1][node.coordinate.x]
                if item.passability != -1:
                    children.append(Map.Node(node, item.coordinate))
            if node.coordinate.y > 0:
                item = map.__map__[node.coordinate.y-1][node.coordinate.x]
                if item.passability != -1:
                    children.append(Map.Node(node, item.coordinate))
            return children

    def calcPath(self, coordinate_from, coordinate_to):

        root = Map.Node(None, coordinate_from)
        root.g = 0.0
        root.h = root.coordinate.getLength(coordinate_to)
        root.f = root.g + root.h

        open_set = []
        open_set.append(root)
        closed_set = []

        while open_set:
            open_set.sort(key=lambda node: node.f)
            best_node = open_set[0]

            if best_node.coordinate == coordinate_to:
                path = []
                node = best_node
                while node:
                    path.insert(0, node.coordinate)
                    node = node.parent
                return path

            open_set.remove(best_node)
            closed_set.append(best_node)

            children = best_node.generateChildren(self)
            for child in children:
                if child in closed_set:
                    continue

                child.g = best_node.g + self.__map__[child.coordinate.y][child.coordinate.x].passability
                child.h = child.coordinate.getLength(coordinate_to)
                child.f = child.g + child.h

                child_from_open_set = None
                for node_from_open_set in open_set:
                    if node_from_open_set == child:
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
coordinate_to = Map.Coordinate(9, 1)
path = map.calcPath(coordinate_from, coordinate_to)
print map.get_str(coordinate_from, coordinate_to, path)
