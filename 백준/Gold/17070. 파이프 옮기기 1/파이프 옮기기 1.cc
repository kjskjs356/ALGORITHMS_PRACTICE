#include <iostream>
#include <queue>
#include <tuple>

#define endl "\n"
#define MAX 16
using namespace std;

int N, ans;
int map[MAX][MAX];
int dx[3] = { 0, 1, 1 };
int dy[3] = { 1, 1, 0 };

int bfs(int a, int b, int d) {
	queue<tuple<int, int, int>> q;
	int x, y, nx, ny;
	q.push({a, b, d});
	while (!q.empty()) {
		x = get<0>(q.front());
		y = get<1>(q.front());
		d = get<2>(q.front());
		q.pop();
		// 목적지 도달할때마다 카운트 증가
		if (x == N - 1 && y == N - 1) ans++;
		for (size_t i = 0; i < 3; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			// 범위 벗어나는지 체크
			if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
				// 대각선 이동 시 이동 칸의 위쪽, 왼쪽 칸도 체크
				if (i == 1) {
					if (map[nx][ny] == 0 && map[nx - 1][ny] == 0 && map[nx][ny - 1] == 0) {
						q.push({ nx, ny, i });
					}
				}
				// 그외에는 이동하려는 칸만 체크
				else if (i == 0 && d != 2) {
					if (map[nx][ny] == 0) {
						q.push({ nx, ny, i });
					}
				}
				else if (i == 2 && d != 0) {
					if (map[nx][ny] == 0) {
						q.push({ nx, ny, i });
					}
				}
			}
		}
	}
	return ans;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> N;
	ans = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin>>map[i][j];
		}
	}
	ans = bfs(0, 1, 0);
	cout << ans;
	return 0;
}
