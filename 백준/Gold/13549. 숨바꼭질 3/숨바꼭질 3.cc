#include <iostream>
#include <queue>

using namespace std;

#define MAX 100001

int N, K;
int ans;
bool visited[MAX];

int bfs() {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({0, N});
	visited[N] = true;
	while (!pq.empty()) {
		int cnt = pq.top().first;
		int x = pq.top().second;
		pq.pop();
		if (x == K) return cnt;
		if (x * 2 >= 0  && x * 2 < MAX && !visited[x * 2]) {
			visited[x * 2] = true;
			pq.push({ cnt, x * 2 });
		}
		if (x + 1 >= 0 && x + 1 <= MAX && !visited[x + 1]) {
			visited[x + 1] = true;
			pq.push({ cnt + 1, x + 1 });
		}
		if (x - 1 >= 0 && x - 1 <= MAX && !visited[x - 1]) {
			visited[x - 1] = true;
			pq.push({ cnt + 1, x - 1 });
		}
	}
}

int main() {
	cin >> N >> K;
	ans = bfs();
	cout << ans;
	return 0;
}