from sys import maxsize
from itertools import permutations
v=4
def tsp(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    nex_permutation=permutations(vertex)
    for i in nex_permutation:
        current_pathweight=0
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            k=j
        current_pathweight+=graph[k][s]
        min_path=min(min_path,current_pathweight)
    return min_path
if __name__=='__main__':
    graph=[[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]]
    s=0
    print(tsp(graph,s))