# Quick Find
class UnionFind:

    def __init__(self, n):
        self.count = n
        self.id = [x for x in range(n)]

    def find(self, p):
        assert 0 <= p < self.count
        return self.id[p]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if q_id == p_id:
            return
        for i in range(self.count):
            if self.id[i] == p_id:
                self.id[i] = q_id
