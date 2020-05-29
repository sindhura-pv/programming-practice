from collections import defaultdict as dd


class Solution:
    def countComponents(self, n: int, edges):

        graph = dd(set)
        vis = set()

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in vis:
                    vis.add(neighbor)
                    dfs(neighbor)

        components = n - len(graph)
        for node in graph:
            if node not in vis:
                vis.add(node)
                dfs(node)
                components += 1

        return components
