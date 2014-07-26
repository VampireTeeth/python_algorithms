class AdjacencySet:

    def __init__(self, vs, ns):
        self.vs = vs
        self.ns = ns

    def neighbours(self, v):
        return self.ns[v]

    def isNeighbour(self, v, n):
        return n in self.ns[v]

    def degree(self, v):
        return len(self.ns[v])

class AdjacencyDict:

    def __init__(self, vs, ns):
        self.vs = vs
        self.ns = ns

    def neighbours(self, v):
        return self.ns[v]

    def isNeighbour(self, v, n):
        return n in self.ns[v]

    def degree(self, v):
        return len(self.ns[v])

    def edgeWeight(self, v1, v2):
        return self.ns[v1][v2]

class AbstractGraph:
    def __init__(self, vs, ns):
        h = [hash(v) for v in vs]
        self.vs = zip(h, vs)
        self.ns = zip(h, ns)
        print h
        print self.vs
        print self.ns

    def neighbours(self, v1):
        pass

    def isNeighbour(self, v1, v2):
        pass

    def degree(self, v):
        pass

    def edgeWeight(self, v1, v2):
        return


def banner(title):
    side = "*" * 10
    return "%s%s%s" % (side, title, side)

def adjacencySetPlay():
    print banner("AdjacencySet")
    vs = range(8)
    a, b, c, d, e, f, g, h = vs
    N = [
        {b, c, d, e, f}, # a
        {c, e}, # b
        {d}, # c
        {e}, # d
        {f}, # e
        {c, g, h}, # f
        {f, h}, # g
        {f, g} # h
    ]

    s = AdjacencySet(vs, N)
    print s.neighbours(a)
    print s.degree(a)
    print s.isNeighbour(a, b)
    print s.isNeighbour(b, a)


def adjacencyDictPlay():
    print banner("AdjacencyDict")
    vs = range(8)
    a, b, c, d, e, f, g, h = vs
    N = [
        {b:2, c:1, d:3, e:9, f:4}, # a
        {c:4, e:3}, # b
        {d:8}, # c
        {e:7}, # d
        {f:5}, # e
        {c:2, g:2, h:2}, # f
        {f:1, h:6}, # g
        {f:9, g:8} # h
    ]
    d = AdjacencyDict(vs, N)
    print d.neighbours(b)
    print d.degree(b)
    print d.isNeighbour(b, e)
    print d.isNeighbour(a, h)
    print d.edgeWeight(b,c)

def abstractGraphPlay():
    print banner("AbstractGraph")
    vs = range(8)
    a, b, c, d, e, f, g, h = vs
    N = [
        {b, c, d, e, f}, # a
        {c, e}, # b
        {d}, # c
        {e}, # d
        {f}, # e
        {c, g, h}, # f
        {f, h}, # g
        {f, g} # h
    ]
    g = AbstractGraph(vs, N)
    pass

if __name__ == '__main__':
    adjacencySetPlay()
    adjacencyDictPlay()
    abstractGraphPlay()

