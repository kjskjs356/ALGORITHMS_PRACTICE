#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>

#define endl "\n"
using namespace std;

int N, m, ans;
int population[11];
int visited[11];
bool chk[11];
vector<int> graph[11];

void dfs(int x, int type) {
	// 각 구역마다 인접한 구역의 개수만큼 순회
	for (int i = 0; i < graph[x].size(); i++) {
		if (chk[graph[x][i]] == false && visited[graph[x][i]] == type) {
			chk[graph[x][i]] = true;
			dfs(graph[x][i], type);
		}
	}
}

bool check() {
	// 1구역 탐색
	for (int i = 1; i <= N; i++) {
		if (visited[i] == 1) {
			chk[i] = true;
			dfs(i, 1);
			break;
		}
	}
	// 2구역 탐색
	for (int i = 1; i <= N; i++) {
		if (visited[i] == 0) {
			chk[i] = true;
			dfs(i, 0);
			break;
		}
	}

	// 연결되지 않은 구역 있으면 패스
	for (int i = 1; i <= N; i++) {
		if (chk[i] == false) return false;
	}
	return true;
}

void back(int cnt) {
	if (cnt == N) {
		memset(chk, false, sizeof(chk));
		if (check()) {
			int sum1 = 0, sum2 = 0;
			for (int i = 1; i <= N; i++) {
				if (visited[i] == 1) sum1 += population[i];
				else sum2 += population[i];
			}
			ans = min(ans, abs(sum1 - sum2));
		}
		return;
	}
	// 모든 경우의 수를 탐색
	visited[cnt + 1] = 1;
	back(cnt + 1);
	visited[cnt + 1] = 0;
	back(cnt + 1);

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	ans = 987654321;
	cin >> N;
	// 인구 수 할당
	for (int i = 1; i <= N; i++) {
		cin >> population[i];
	}
	// 각 구역별 인접구역 설정
	for (int i = 1; i <= N; i++) {
		// 인접 구역의 개수
		cin >> m;
		// 인접 구역 동적 할당
		for (int j = 0; j < m; j++) {
			int num;
			cin >> num;
			graph[i].push_back(num);
		}
	}
	back(0);
	if (ans == 987654321) cout << -1;
	else cout << ans;
	return 0;
}