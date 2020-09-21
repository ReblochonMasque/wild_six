import itertools

class Node:
    def __init__(self, name, position):
        self.__name__ = name
        self.__position__ = position
    def __eq__(self, other):
        assert isinstance(other, Node)
        return self.__position__ == other.__position__
    def __lt__(self, other):
        assert isinstance(other, Node)
        return self.__position__ < other.__position__
    def __hash__(self):
        return hash(self.__repr__())
    def __repr__(self):
        return self.__name__

class Edge:
    def __init__(self, node1, node2):
        assert isinstance(node1, Node)
        assert isinstance(node2, Node)
        self.node1, self.node2 = sorted([node1, node2])

    def __lt__(self,other):
        return self.node1 < other.node1

    def incident(self, other):
        c1 = set([self.node1.__name__, self.node2.__name__])
        c2 = set([other.node1.__name__, other.node2.__name__])
        c3 = c1.intersection(c2)
        # print(f'c1 = {c1}')
        # print(f'c2 = {c2}')
        # print(f'c3 = {c3}')
        return len(c3)>0

    def meet(self, other):
        c1 = set([self.node1.__name__, self.node2.__name__])
        c2 = set([other.node1.__name__, other.node2.__name__])
        c3 = c1.union(c2)
        return len(c3)==4

    def __repr__(self):
        return self.node1.__name__+self.node2.__name__

class Meet:
    def __init__(self, edge1, edge2):
        assert isinstance(edge1, Edge)
        assert isinstance(edge2, Edge)
        assert edge1.meet(edge2)
        self.edge1, self.edge2 = sorted([edge1, edge2])

    def __repr__(self):
        return self.edge1.__repr__() + '.' +self.edge2.__repr__()

class Nodes:
    def __init__(self, nodes):
        assert isinstance(nodes,(list,str))
        assert len(set(nodes)) == len(nodes)
        self.__max_nodes__ = len(nodes)
        self._n = [Node(nodes[i],i) for i in range(self.__max_nodes__)]
        self.__nodes__ = dict(list(zip([x.__name__ for x in self._n], self._n)))

    def edges(self):
        L = []
        for x in itertools.combinations(self.__nodes__,2):
            e = Edge(self[x[0]],self[x[1]])
            L.append(e)
        return L

    def meets(self):
        return [Meet(x,y) for x,y in itertools.combinations(self.edges(),2) if x.meet(y)]

    def __getitem__(self, i):
        return self.__nodes__[i]

    def __repr__(self):
        s = ','.join([v.__name__ for k,v in self.__nodes__.items()])
        return  f'Nodes({self.__max_nodes__}) = {s}'

class BadData(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class LOMS:
    def __init__(self, from_nodes, nodes_labels):
        assert isinstance(from_nodes, Nodes)
        for x in nodes_labels:
            try:
                assert (x in from_nodes.__nodes__)
            except:
                raise BadData(f"node {x} is not part of allowed nodes: {from_nodes}")
        self.from_nodes = from_nodes
        self.nodes_labels = nodes_labels
        self.nodes = [self.from_nodes[x] for x in nodes_labels]

class List(LOMS):
    def __init__(self, from_nodes, nodes_labels):
        super().__init__(from_nodes, nodes_labels)

    def __eq__(self, other):
        c0 = self.nodes_labels==other.nodes_labels
        c1 = self.from_nodes==other.from_nodes
        return c0 and c1

    def __repr__(self):
        s = ', '.join([k.__name__ for k in self.nodes])
        n = len(self.nodes)
        return  f'{n}-List = [{s}]'

class Set(LOMS):
    def __init__(self, from_nodes, nodes_labels):
        super().__init__(from_nodes, nodes_labels)
        try:
            assert len(set(nodes_labels)) == len(nodes_labels)
        except:
            raise BadData(f"duplicate nodes are not allowed in Set: {nodes_labels}")

    def __eq__(self, other):
        return set(self.nodes_labels) == set(other.nodes_labels)

    def __repr__(self):
        s = ' '.join([k.__name__ for k in self.nodes])
        n = len(self.nodes)
        return  f'{n}-Set = [{s}]'

class Oset(LOMS):
    def __init__(self, from_nodes, nodes_labels):
        super().__init__(from_nodes, nodes_labels)
        try:
            assert len(set(nodes_labels)) == len(nodes_labels)
        except:
            raise BadData(f"duplicate nodes are not allowed in Set: {nodes_labels}")

    def __eq__(self, other):
        return self.nodes_labels == other.nodes_labels

    def __repr__(self):
        s = ', '.join([k.__name__ for k in self.nodes])
        n = len(self.nodes)
        return  f'{n}-Oset = [{s}]'

class Mset(LOMS):
    def __init__(self, from_nodes, nodes_labels):
        super().__init__(from_nodes, nodes_labels)

    def __eq__(self, other):
        return set(self.nodes_labels) == set(other.nodes_labels)

    def __repr__(self):
        s = ' '.join([k.__name__ for k in self.nodes])
        n = len(self.nodes)
        return  f'{n}-Mset = [{s}]'

if __name__=='__main__':
    pass
