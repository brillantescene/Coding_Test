# 일정 재구성
from collections import defaultdict


def findItinerary(tickets):

    def dfs(v):
        while graph[v]:
            dfs(graph[v].pop(0))
        route.append(v)

    graph = defaultdict(list)
    print(sorted(tickets))
    print(sorted(tickets, reverse=True))
    for frm, to in sorted(tickets, reverse=True):
        graph[frm].append(to)
    print(graph)
    route = []
    dfs('JFK')
    return route[::-1]


print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
