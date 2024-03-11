# 1389 케빈 베이컨의 6단계 법칙

import heapq
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(graph, start):
    distances = [int(1e9)] * (N + 1)
    distances[0] = 0
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

    return distances

answer = 1e9
for i in range(1, N + 1):
    result = sum(dijkstra(graph, i))
    if result < answer:
        answer = result
        number = i

print(number)
