class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def kruskal_mst(self):
        # Sort edges based on their weights
        self.graph.sort(key=lambda item: item[2])

        parent = list(range(self.V))
        rank = [0] * self.V

        mst = []

        for u, v, w in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # If including this edge doesn't form a cycle
            if root_u != root_v:
                mst.append([u, v, w])
                self.union(parent, rank, root_u, root_v)

            # Stop if we already have V-1 edges in MST
            if len(mst) == self.V - 1:
                break

        return mst


# Example usage
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = g.kruskal_mst()
print("Edges in the constructed MST:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
