# 백준 1261 알고스팟
import heapq



M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra(arr):
    distances = [[int(1e9)] * M for _ in range(N)]
    distances[0][0] = 0
    queue = []
    heapq.heappush(queue, [distances[0][0], 0, 0])

    while queue:
        dist, x, y = heapq.heappop(queue)

        if distances[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                distance = dist + arr[nx][ny]
                if distance < distances[nx][ny]:
                    distances[nx][ny] = distance
                    heapq.heappush(queue, [distance, nx, ny])
    return distances[N-1][M-1]

result = dijkstra(arr)
print(result)