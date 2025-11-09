from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def ae(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
if __name__=='__main__':
    g=graph()
    g.ae(0,1)
    g.ae(0,2)
    g.ae(2,2)
    g.ae(2,0)
    g.ae(2,3)
    g.ae(3,3)
    print("BFS:")
    g.bfs(2)