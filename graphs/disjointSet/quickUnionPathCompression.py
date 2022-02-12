class UninonSet:
    def __init__(self, size) -> None:
        # [0, 1, 2, 3, 4....]
        self.root = [i for i in range(size)]

    def find(self, v):
        if v == self.root[v]:
            return v

        self.root[v] = self.find(self.root[v])
        return self.root[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        # if root1 != root2:
        self.root[root2] = root1

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

# Tests


u = UninonSet(10)
u.union(0, 1)
u.union(1, 2)
u.union(2, 3)
u.union(3, 4)
u.union(4, 5)

u.find(5)

print(u.root)
