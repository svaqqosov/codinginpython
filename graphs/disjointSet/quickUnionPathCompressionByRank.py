class UninonSet:
    def __init__(self, size) -> None:
        # [0, 1, 2, 3, 4....]
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, v):
        if v == self.root[v]:
            return v

        self.root[v] = self.find(self.root[v])
        return self.root[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        else:
            self.root[root1] = root2
            self.rank[root1] += 1

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

# Tests


uf = UninonSet(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

print(uf.root)
print(uf.rank)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
