#include <iostream>
#include <deque>

using namespace std;

#define MAX 1001

int N, M, V;
bool visited[MAX];
int graph[MAX][MAX];

void reset() {
	for (int i = 0; i < MAX; i++) {
		visited[i] = false;
	}
}

void dfs(int x) {
	visited[x] = true;
	cout << x << ' ';
	for (int i = 0; i <= N; i++) {
		if (graph[x][i] == 1 && visited[i] == false) {
			dfs(i);
		}
	}
}

void bfs(int x) {
	deque<int> q;
	q.push_back(x);
	while (!q.empty()) {
		x = q.front();
		visited[x] = true;
		cout << x << ' ';
		q.pop_front();
		for (int i = 0; i <= N; i++) {
			if (graph[x][i] == 1 && visited[i] == false) {
				visited[i] = true;
				q.push_back(i);
			}
		}
	}
}

int main() {
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++) {
		int s, e;
		cin >> s >> e;
		graph[s][e] = 1;
		graph[e][s] = 1;
	}
	dfs(V);
	reset();
	cout << '\n';
	bfs(V);

}