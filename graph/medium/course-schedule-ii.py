from collections import defaultdict as dd


class Solution:
    def findOrder(self, n: int, edges):

        graph = dd(set)
        vis = set()

        for u, v in edges:
            graph[u].add(v)

        def hasCycle(graph):

            if not graph:
                return False

            vis = set()

            def hasCycleHelper(node, graph, vis, stack):

                vis.add(node)
                stack.add(node)

                for neighbor in graph[node]:
                    if neighbor not in vis:
                        if hasCycleHelper(neighbor, graph, vis, stack):
                            return True
                    elif neighbor in stack:
                        return True

                stack.remove(node)
                return False

            for node in list(graph):
                if node not in vis:
                    if hasCycleHelper(node, graph, vis, set()):
                        return True

            return False

        def topSort(graph, n):

            result = []
            vis = set()

            def topSortUtil(node):

                vis.add(node)
                for neighbor in graph[node]:
                    if neighbor not in vis:
                        topSortUtil(neighbor)

                result.append(node)

            for node in list(graph):
                if node not in vis:
                    topSortUtil(node)

            for i in range(n):
                if i not in vis:
                    result.append(i)

            return result

        return [] if hasCycle(graph) else topSort(graph, n)