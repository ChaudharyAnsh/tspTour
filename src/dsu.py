class DSU:
    def __init__(self, n):
        self.n = n
        self.head = [i for i in range(self.n)]
        self.size = [1 for i in range(self.n)]

    # set find
    def find(x):
        if self.head[x] == x:
            return x
        self.head[x] = find(self.head[x])
        return self.head[x]

    # set union
    def union(x, y):
        head_x, head_y = find(x), find(y)
        if head_x == head_y:
            return
        if self.size[head_x] <= self.size[head_y]:
            self.head[head_x] = head_y
            self.size[head_y] += self.size[head_x]
        else:
            self.head[head_y] = head_x
            self.size[head_x] += self.size[head_y]
