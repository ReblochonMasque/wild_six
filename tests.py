from wild_six import Nodes, Node, Set, List, Mset, Oset, BadData

N = Nodes(nodes='1b3456')
print(N)

assert N['1'] < N['b']

s1 = Set(from_nodes=N, nodes_labels=['1','3'])
print(s1)
s2 = Set(from_nodes=N, nodes_labels=['3','1'])
assert s1==s2

try:
    s = Set(from_nodes=N, nodes_labels=['1','1'])
except BadData as e:
    print(e)

try:
    s = Set(from_nodes=N, nodes_labels=['x','1'])
except BadData as e:
    print(e)

l1 = List(from_nodes=N, nodes_labels=['1','3', 'b', '3'])
print(l1)
l2 = List(from_nodes=N, nodes_labels=['1','3', 'b'])
try:
    assert l1 == l2
except AssertionError as e:
    print('l1 != l2')

m1 = Mset(from_nodes=N, nodes_labels=['b','b','1'])
print(m1)

o1 = Oset(from_nodes=N, nodes_labels=['1','3','b','4'])
print(o1)

edges = N.edges()
print(edges)
assert edges[0].incident(edges[1])
assert not edges[0].incident(edges[14])
#
assert len(N.meets())==45
