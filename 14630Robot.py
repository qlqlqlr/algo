# 백준 14630 변신하는 로봇

import heapq

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
s, e = map(int, input().split())
length = len(arr[0])


def dijkstra(arr, s, e):
    distances = [int(1e9)] * (N + 1)
    distances[s] = 0
    queue = []
    heapq.heappush(queue, [distances[s], s])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for i in range(N):
            if i == node - 1:
                continue
            else:

                next_node = i + 1
                next_dist = 0
                for j in range(length):
                    next_dist += (arr[i][j] - arr[node-1][j])**2

                distance = next_dist + dist
                if distance < distances[next_node]:
                    distances[next_node] = distance
                    heapq.heappush(queue, [distance, next_node])

    return distances[e]

result = dijkstra(arr, s, e)
print(result)

