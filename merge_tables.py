class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
        self.max_size = max(self.size)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.max_size = max(self.max_size, self.size[root_x])

    def get_max_size(self):
        return self.max_size

def merge_tables(n, m, rows, queries):
    dsu = DisjointSetUnion(n)
    result = []

    for d, s in queries:
        d, s = d - 1, s - 1  # Convert 1-based indexing to 0-based indexing
        dsu.union(d, s)
        result.append(dsu.get_max_size())

    return result

# Read input
n, m = map(int, input().split())
rows = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]

# Solve the problem
result = merge_tables(n, m, rows, queries)

# Print the output
for res in result:
    print(res)
