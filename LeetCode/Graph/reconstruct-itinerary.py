from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(v):
            while graph[v]:
                dfs(graph[v].pop(0))
            route.append(v)

        graph = defaultdict(list)
        for frm, to in sorted(tickets):
            graph[frm].append(to)
        route = []
        dfs('JFK')
        return route[::-1]
