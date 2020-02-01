from collections import defaultdict as dd


class Solution:
    def findRedundantConnection(self, edges):

        graph = dd(set)

        def dfs(s, t):

            if s not in seen:
                seen.add(s)
                if s == t:
                    return True

                return any(dfs(neighbor, t) for neighbor in graph[s])

            return False

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)