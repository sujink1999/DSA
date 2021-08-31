# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        weights = [0]*n
        depths = [0]*n
        distances = [0]*n
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
        def find(node, parent, depth):
            weight = 1
            for neigh in g[node]:
                if neigh != parent:
                    weight += find(neigh, node, depth+1) 
            depths[node] = depth
            weights[node] = weight
            return weight
        find(0,-1,0)
        def findDistances(node, parent, dist):
            distances[node] = dist
            for neigh in g[node]:
                if parent != neigh:
                    findDistances(neigh, node, dist - weights[neigh] + (n - weights[neigh]))
        findDistances(0, -1, sum(depths))
        return distances