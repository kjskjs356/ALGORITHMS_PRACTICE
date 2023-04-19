#include <iostream>
#include <queue>
using namespace std;

#define endl '\n'

const int INF = 987654321;

int V, E;
int start;
int u, v, w;
int dist[20001];
vector<pair<int, int>> g[20001];

void dijk(int s) {
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

	cin >> V >> E;
	cin >> start;
	for (int i = 0; i < E; ++i) {
		cin >> u >> v >> w;
		g[u].push_back({ v, w });
	}
	// 거리 INF로 초기화
	for (int i = 1; i <= V; ++i) dist[i] = INF;
	// 시작점은 거리 0
	dist[start] = 0;

	dijk(start);
	for (int i = 1; i <= V; ++i) {
		if (dist[i] == INF) cout << "INF" << endl;
		else cout << dist[i] << endl;
	}


	return 0;
}