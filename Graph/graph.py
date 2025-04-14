from typing import List, Dict, Tuple, Generator
from Stack.stack import Stack
from Queue.queue import Queue


class Graph:
    def __init__(self) -> None:
        self._vertices: List[str] = []  # List of vertex labels like ['A', 'B', 'C']
        self._adjMat: Dict[Tuple[int, int], int] = {}  # Adjacency matrix using dictionary of vertex index pairs

    def nVertices(self) -> int:
        """Return total number of vertices"""
        return len(self._vertices)

    def nEdges(self) -> int:
        """Return number of edges (undirected, so divide by 2)"""
        return len(self._adjMat) // 2

    def addVertex(self, vertex: str) -> None:
        """Add a vertex label like 'A', 'B', etc."""
        self._vertices.append(vertex)

    def validIndex(self, n: int) -> bool:
        """Check if index is within range of vertices"""
        if n < 0 or self.nVertices() <= n:
            raise IndexError("Invalid vertex index")
        return True

    def getVertex(self, n: int) -> str:
        """Return the label of the vertex at index n"""
        if self.validIndex(n):
            return self._vertices[n]

    def addEdge(self, A: int, B: int) -> None:
        """Add undirected edge between vertex A and B"""
        self.validIndex(A)
        self.validIndex(B)
        if A == B:
            raise ValueError("Pseudographs (loops) not allowed")
        self._adjMat[(A, B)] = 1
        self._adjMat[(B, A)] = 1

    def hasEdge(self, A: int, B: int) -> bool:
        """Check if there is an edge between A and B"""
        self.validIndex(A)
        self.validIndex(B)
        return self._adjMat.get((A, B), False)   # If it doesn’t exist, it returns False by default

    def vertices(self) -> range:
        """Return all valid vertex indices"""
        return range(self.nVertices())

    def adjacentVertices(self, n: int) -> Generator[int, None, None]:
        """Yield all adjacent vertex indices of vertex n"""
        self.validIndex(n)
        for j in self.vertices():
            if j != n and self.hasEdge(n, j):
                yield j   # Yields (like returns, but one at a time in a loop)

    def adjacentUnvisitedVertices(self, n: int, visited: List[bool], markVisits: bool = True) -> Generator[int, None, None]:
        """Yield adjacent vertices to n that haven't been visited yet"""
        for j in self.adjacentVertices(n):
            if not visited[j]:
                if markVisits:
                    visited[j] = True
                yield j

    def depthFirst(self, n: int) -> None:
        """Perform depth-first search from vertex index n"""
        self.validIndex(n)
        visited: List[bool] = [False] * self.nVertices()
        stack = Stack(100)
        stack.push(n)
        visited[n] = True
        print("DFS Traversal:")
        print(self.getVertex(n), end=' ')  # Only print when visiting the node

        while not stack.isEmpty():
            visit = stack.peek()
            found = False
            for adj in self.adjacentUnvisitedVertices(visit, visited):
                stack.push(adj)
                visited[adj] = True  # mark as visited when pushing
                print(self.getVertex(adj), end=' ')  # print when visiting
                found = True
                break  # go deeper
            if not found:
                stack.pop()
        print()

    def depthFirstRecursive(self, n: int) -> None:
        """Recursive depth-first search starting from vertex index n"""
        self.validIndex(n)
        visited = [False] * self.nVertices()
        print("DFS Recursive Traversal:")
        self._dfs_recursive_helper(n, visited)
        print()

    def _dfs_recursive_helper(self, n: int, visited: List[bool]) -> None:
        visited[n] = True
        print(self.getVertex(n), end=' ')
        for j in self.adjacentUnvisitedVertices(n, visited):
            self._dfs_recursive_helper(j, visited)

    def breadthFirst(self, n: int) -> None:
        """Perform breadth-first search from vertex index n"""
        self.validIndex(n)
        visited: List[bool] = [False] * self.nVertices()
        queue = Queue(100)
        queue.insert(n)
        visited[n] = True
        print("BFS Traversal:")

        while not queue.isEmpty():
            visit = queue.remove()
            print(self.getVertex(visit), end=' ')
            for j in self.adjacentUnvisitedVertices(visit, visited):
                queue.insert(j)
        print()


if __name__ == "__main__":
    g = Graph()

    # Add vertices with labels
    for label in ['A', 'B', 'C', 'D', 'E']:
        g.addVertex(label)

    # Create undirected edges by vertex indices
    g.addEdge(0, 1)  # A-B
    g.addEdge(0, 2)  # A-C
    g.addEdge(1, 3)  # B-D
    g.addEdge(2, 4)  # C-E
    g.addEdge(3, 4)  # D-E

    # Traversal outputs
    g.depthFirst(0)  # Output: A B D E C
    g.depthFirstRecursive(0)
    g.breadthFirst(0)  # Output: A B C D E
