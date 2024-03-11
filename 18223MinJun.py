import heapq
import sys
input = sys.stdin.readline

V, E, P = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(graph, start, end):
    distances = [int(1e9)] * (V + 1)
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

success = dijkstra(graph, 1, P) + dijkstra(graph, P, V)
fail = dijkstra(graph,1, V)


if success == fail:
    print("SAVE HIM")
else:
    print("GOOD BYE")