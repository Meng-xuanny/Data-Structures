import math

# Define a Point class
class Point:
    def __init__(self, x, y, label=None):
        self.x = x
        self.y = y
        self.label = label  # optional data label

    def __repr__(self):
        return f"({self.x}, {self.y}) {self.label if self.label else ''}"


# Define a QuadTree Node
class QuadTreeNode:
    def __init__(self, point, boundary):
        self.point = point  # the (x, y) point
        self.boundary = boundary  # rectangle this node covers
        self.NE = None
        self.NW = None
        self.SE = None
        self.SW = None


# Define the boundary rectangle
class Rectangle:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    # Checks if a point lies within the rectangle
    def contains(self, point):
        return self.x_min <= point.x < self.x_max and self.y_min <= point.y < self.y_max

    # checks if the current node could possibly contain a closer point.
    def intersects_circle(self, x, y, radius):
        # Check if a circle centered at (x, y) intersects this rectangle
        closest_x = max(self.x_min, min(x, self.x_max))
        closest_y = max(self.y_min, min(y, self.y_max))
        dx = x - closest_x
        dy = y - closest_y
        return dx * dx + dy * dy <= radius * radius


# QuadTree class
class QuadTree:
    def __init__(self, boundary):
        self.root = None
        self.boundary = boundary

    def insert(self, point):
        def _insert(node, point, boundary):
            # Base Case: Empty spot found
            if node is None:
                return QuadTreeNode(point, boundary)

            # Decide quadrant
            mid_x = (boundary.x_min + boundary.x_max) / 2
            mid_y = (boundary.y_min + boundary.y_max) / 2

            if point.x >= mid_x:
                if point.y >= mid_y:
                    # Give it a rectangle that represents the top-right portion of the current one
                    child_boundary = Rectangle(mid_x, boundary.x_max, mid_y, boundary.y_max)
                    node.NE = _insert(node.NE, point, child_boundary) # insert the node into the rectangle
                    # recursively tries to insert deeper in the NE subtree
                else:
                    child_boundary = Rectangle(mid_x, boundary.x_max, boundary.y_min, mid_y)
                    node.SE = _insert(node.SE, point, child_boundary)
            else:
                if point.y >= mid_y:
                    child_boundary = Rectangle(boundary.x_min, mid_x, mid_y, boundary.y_max)
                    node.NW = _insert(node.NW, point, child_boundary)
                else:
                    child_boundary = Rectangle(boundary.x_min, mid_x, boundary.y_min, mid_y)
                    node.SW = _insert(node.SW, point, child_boundary)

            return node

        self.root = _insert(self.root, point, self.boundary)

    def find(self, x, y):
        def _find(node, x, y):
            if node is None:
                return None
            if node.point.x == x and node.point.y == y:
                return node.point
            mid_x = (node.boundary.x_min + node.boundary.x_max) / 2
            mid_y = (node.boundary.y_min + node.boundary.y_max) / 2

            if x >= mid_x:
                if y >= mid_y:
                    return _find(node.NE, x, y)
                else:
                    return _find(node.SE, x, y)
            else:
                if y >= mid_y:
                    return _find(node.NW, x, y)
                else:
                    return _find(node.SW, x, y)

        return _find(self.root, x, y)

    def find_nearest(self, x, y):
        # best[0] holds the current best (closest) point.
        # best[1] holds the current shortest distance found (initialized to infinity).
        best = [None, float('inf')]

        # looking for the nearest point to (x, y)
        def _search(node):
            if node is None:
                return
            dist = math.hypot(x - node.point.x, y - node.point.y)
            if dist < best[1]:  # If it’s closer than the current best, update best
                best[0] = node.point
                best[1] = dist

            mid_x = (node.boundary.x_min + node.boundary.x_max) / 2
            mid_y = (node.boundary.y_min + node.boundary.y_max) / 2

            # Choose order based on target point
            quadrants = []
            if x >= mid_x:
                if y >= mid_y:
                    quadrants = [node.NE, node.NW, node.SE, node.SW]
                else:
                    quadrants = [node.SE, node.SW, node.NE, node.NW]
            else:
                if y >= mid_y:
                    quadrants = [node.NW, node.NE, node.SW, node.SE]
                else:
                    quadrants = [node.SW, node.SE, node.NW, node.NE]

            for q in quadrants:
                if q and q.boundary.intersects_circle(x, y, best[1]):
                    _search(q)

        _search(self.root)
        return best[0]


def print_quadtree(node, level=0, quadrant='Root'):
    if node is None:
        return
    indent = '    ' * level
    print(f"{indent}{quadrant}: Point{node.point}")

    print_quadtree(node.NW, level + 1, 'NW')
    print_quadtree(node.NE, level + 1, 'NE')
    print_quadtree(node.SW, level + 1, 'SW')
    print_quadtree(node.SE, level + 1, 'SE')

if __name__ == "__main__":
    boundary = Rectangle(0, 100, 0, 100)
    tree = QuadTree(boundary)

    points = [
        Point(30, 40, "A"),
        Point(60, 70, "B"),
        Point(20, 90, "C"),
        Point(85, 10, "D"),
        Point(55, 55, "E")
    ]

    for pt in points:
        tree.insert(pt)

    print("\n--- Quad Tree Structure ---")
    print_quadtree(tree.root)

    print("\nFind (20, 90):", tree.find(20, 90))
    print("Nearest to (50, 50):", tree.find_nearest(50, 50))

