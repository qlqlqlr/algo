# 백준 1238 파티
import heapq
import sys
input = sys.stdin.readline


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

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

answer = 0
for i in range(1, N + 1):
    if i == X:
        continue
    result = dijkstra(graph, i, X) + dijkstra(graph, X, i)
    if result > answer:
        answer = result

print(answer)
