# 백준 4485번 녹색 옷 입은 애가 젤다지?
import heapq
import sys
input = sys.stdin.readline

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

cnt = 0

def dijkstra(arr):
    distances = [[int(1e9)] * N for _ in range(N)]
    distances[0][0] = arr[0][0]
    queue = []
    heapq.heappush(queue, [distances[0][0], 0, 0])

    while queue:
        dist, node1, node2 = heapq.heappop(queue)

        if distances[node1][node2] < dist:
            continue

        for i in range(4):
            nx = node1 + dir_x[i]
            ny = node2 + dir_y[i]
            if 0 <= nx < N and 0 <= ny < N:
                distance = dist + arr[nx][ny]
                if distance < distances[nx][ny]:
                    distances[nx][ny] = distance
                    heapq.heappush(queue, [distance, nx, ny])
    return distances[N-1][N-1]


while 1:

    N = int(input())
    cnt += 1

    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(arr)
    print(f'Problem {cnt}: {result}')
