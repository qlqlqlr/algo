# 백준 1504 특정한 최단 경로

import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
start = 1

def dijkstra(graph, start, end):
    distances = [int(1e9)] * (N + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])

    return distances[end]

result1 = dijkstra(graph, start, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, N)
result2 = dijkstra(graph, start, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, N)


if result1 >= int(1e9) and result2 >= int(1e9):
    print(-1)
else:
    print(min(result2, result1))

