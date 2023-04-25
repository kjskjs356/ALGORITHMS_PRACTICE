#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

#define endl '\n'

const int INF = 987654321;

int N, M;
int ans;
int u, v, w;
int s, e;
int dist[1001];
vector<pair<int, int>> g[1001];

void dijk(int s) {
	// 거리 INF로 초기화
	for (int i = 1; i <= N; ++i) dist[i] = INF;
	// 시작점은 거리 0
	dist[s] = 0;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	// 시작점의 위치와 거리
	pq.push({ 0, s });
	while (!pq.empty()) {
		int now = pq.top().second;
		int d = pq.top().first;
		pq.pop();
		if (dist[now] < d) continue;
		for (int i = 0; i < g[now].size(); ++i) {
			int next = g[now][i].first;
			int next_d = g[now][i].second;
			if (dist[next] > d + next_d) {
				dist[next] = d + next_d;
				pq.push({dist[next], next});
			}
		}
	}
}

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;
	for (int i = 0; i < M; ++i) {
		cin >> u >> v >> w;
		g[u].push_back({ v, w });
	}
	cin >> s >> e;
	// 각 사람마다 최단거리 계산후 값 저장
	dijk(s);
	ans = dist[e];

	cout << ans;

	return 0;
}