class Coordinate(object):
    def __init__(coordinate, x, y):
        coordinate.x = x
        coordinate.y = y

    def __eq__(point1, point2):
        return point1.x == point2.x and point1.y == point2.y

    def getLength(point1, point2):
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

class Area(object):
    def __init__(area):
        area.passabilities = [
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
        area.widht = len(area.passabilities[0])
        area.height = len(area.passabilities)

    def getPassability(area, coordinate):
        return area.passabilities[coordinate.y][coordinate.x];

    def toString(area, coordinate_from, coordinate_to, path):
        result = ''
        coordinate = Coordinate(0, 0)
        for passabilities_row in area.passabilities:
            if result:
                result += '\n'
            for passability in passabilities_row:
                if coordinate_from == coordinate:
                    result += ' OO'
                elif coordinate_to == coordinate:
                    result += ' XX'
                else:
                    path_item_found = None
                    for path_item in path:
                        if path_item == coordinate:
                            path_item_found = path_item
                            break

                    if path_item_found:
                        result += '  *'
                    elif passability == -1:
                        result += ' ##'
                    elif passability == 1:
                        result += '  .'
                    else:
                        result += '%3d' % passability

                coordinate.x += 1

            coordinate.x = 0
            coordinate.y += 1

        return result

    class Node(object):
        def __init__(node, parent, coordinate):
            node.parent = parent
            node.coordinate = coordinate
            node.f = 0.0
            node.g = 0.0
            node.h = 0.0

        def __eq__(node1, node2):
            return node1.coordinate == node2.coordinate

        def generateChildren(node, area):
            children = []
            coordinates = [
                Coordinate(node.coordinate.x+1, node.coordinate.y),
                Coordinate(node.coordinate.x-1, node.coordinate.y),
                Coordinate(node.coordinate.x, node.coordinate.y+1),
                Coordinate(node.coordinate.x, node.coordinate.y-1)]
            for coordinate in coordinates:
                child = node.generateChild(coordinate, area)
                if child:
                    children.append(child)
            return children

        def generateChild(node, coordinate, area):
            if coordinate.x < 0 or area.widht <= coordinate.x:
                return None
            if coordinate.y < 0 or area.height <= coordinate.y:
                return None

            if area.getPassability(coordinate) == -1:
                return None

            return Area.Node(node, coordinate)

    def getPath(area, coordinate_from, coordinate_to):

        root = Area.Node(None, coordinate_from)
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

            children = best_node.generateChildren(area)
            for child in children:
                if child in closed_set:
                    continue

                child.g = best_node.g + area.getPassability(child.coordinate)
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

area = Area()
coordinate_from = Coordinate(2, 3)
coordinate_to = Coordinate(9, 1)
path = area.getPath(coordinate_from, coordinate_to)
print area.toString(coordinate_from, coordinate_to, path)
