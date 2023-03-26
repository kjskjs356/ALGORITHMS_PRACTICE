#include <iostream>

using namespace std;

int n, s, e, m,  x, y;
int cnt = 0;
int graph[101][101] = { 0, };
int visited[101] = {false, };
int ans = 987654321;

void dfs(int x, int cnt) {
	int start = x;
	if (start == e) {
		ans = cnt;
	}
	for (int i = 0; i < 101; i++) {
		if (graph[x][i] == 1 && !visited[i]) {
			visited[i] = true;
			dfs(i, cnt + 1);
		}
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	cin >> s >> e;
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		graph[x][y] = 1;
		graph[y][x] = 1;
	}
	visited[s] = true;
	dfs(s, cnt);
	if (ans == 987654321) cout << -1;
	else cout << ans;

	return 0;
}