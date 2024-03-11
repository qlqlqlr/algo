import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 노드와 간선수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split())

def dijkstra(graph, start):
    distances = [int(1e9)] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue)


        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distnace = dist + next_dist
            if distnace < distances[next_node]:
                distances[next_node] = distnace
                heapq.heappush(queue, [distnace, next_node])
    return distances

result = dijkstra(graph, start)
print(result[end])