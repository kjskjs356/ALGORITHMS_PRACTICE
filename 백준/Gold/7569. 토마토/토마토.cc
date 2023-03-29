#include <iostream>
#include <algorithm>
#include <deque>
#include <vector>

#define endl "\n"
using namespace std;

int M, N, H, cnt, temp_cnt;
int map[100][100][100];
int ans = 0;
bool flag;
int zero = 0;
// 익어있는 토마토 좌표 동적 배열
deque<pair<pair<int, int>, int>> t;

int dx[] = { 1, -1, 0, 0 };
int dy[] = { 0, 0, 1, -1 };

void bfs() {
	cnt = t.size();
	temp_cnt = 0;
	while (cnt--) {
		// 층, 행, 열
		int z, x, y, nz, nx, ny;
		z = t.front().first.first;
		x = t.front().first.second;
		y = t.front().second;
		t.pop_front();
		// 상하좌우 4방향 먼저 탐색
		for (int i = 0; i < 4; ++i) {
			nx = x + dx[i];
			ny = y + dy[i];
			if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
				// 익지 않은 토마토면 익히고 덱에 추가
				if (map[z][nx][ny] == 0) {
					flag = true;
					--zero;
					map[z][nx][ny] = 1;
					t.push_back({ {z, nx}, ny });
					++temp_cnt;
				}
			}
		}
		// 위, 아래 층 탐색
		for (int layer : {-1, 1}) {
			nz = z + layer;
			if (nz >= 0 && nz < H) {
				if (map[nz][x][y] == 0) {
					flag = true;
					--zero;
					map[nz][x][y] = 1;
					t.push_back({ {nz, x}, y });
					++temp_cnt;
				}
			}
		}
	}
	cnt = temp_cnt;
	temp_cnt = 0;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ans = 0;


	cin >> M >> N>> H;
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < N; ++j) {
			for (int k = 0; k < M; ++k) {
				cin >> map[i][j][k];
				if (map[i][j][k] == 0) ++zero;
				else if (map[i][j][k] == 1) t.push_back({ {i, j }, k });
			}
		}
	}
	// 처음부터 모든 토마토가 익어있는 상태
	if (zero == 0) {
		cout << 0 << endl;
		return 0;
	}
	while (true) {
		++ans;
		flag = false;
		bfs();
		// 토마토가 더이상 익지 못하는데 0이 남아있으면 -1 출력
		if (!flag) {
			cout << -1;
			return 0;
		}
		//토마토가 1개이상 익은게 발생하고 안익은 토마토가 없으면 ans 출력
		else {
			if (zero == 0) {
				cout << ans;
				return 0;
			}
		}
	}


	return 0;
}