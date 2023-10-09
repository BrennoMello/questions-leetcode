from typing import List
from queue import Queue 
from collections import defaultdict

class Solution:
   
    #Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    #Output: true
    #Explanation: There are two paths from vertex 0 to vertex 2:
    #- 0 → 1 → 2
    #- 0 → 2

   
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph_map = defaultdict(list)
        for index, vertex in edges:
            print(index)
            
            graph_map[index].append(vertex)
            graph_map[vertex].append(index)

        print(graph_map)
        visited = list()
        visited.append(source)
        
        queue = Queue()
        queue.put(source)

        while(queue.empty() == False):
            #current = graph_map[queue.get()]
            current = queue.get()
            if current == destination:
                    return True
            
            for vertex in graph_map[current]:
                
                if vertex not in visited:
                    queue.put(vertex)
                    visited.append(vertex)

        return False;

solution = Solution()
print(solution.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))
print(solution.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
