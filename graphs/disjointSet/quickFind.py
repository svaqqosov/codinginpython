class UninonSet:
    def __init__(self, size) -> None:
        # [0, 1, 2, 3, 4....]
        self.root = [i for i in range(size)]

    def find(self, v):
        return self.root[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            for i in range(len(self.root)):
                if self.root[i] == root2:
                    self.root[i] = root1

        return None

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

# Tests


u = UninonSet(10)
u.union(0, 1)
u.union(0, 2)
u.union(1, 3)
u.union(3, 6)

u.union(5, 7)

u.union(4, 8)

print(u.root)

print(u.find(3))
print(u.find(7))
print(u.connected(1, 3))
print(u.connected(0, 2))
print(u.connected(7, 8))
print(u.connected(9, 3))
