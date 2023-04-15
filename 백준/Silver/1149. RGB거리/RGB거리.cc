#include <iostream>
#include <vector>

using namespace std;

#define endl '\n'

int N;
int r, g, b;
int map[1001][3];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N;
	map[0][0] = 0;
	map[0][1] = 0;
	map[0][2] = 0;
	for (int i = 1; i <= N; ++i) {
		cin >> r >> g >> b;
		map[i][0] = min(map[i - 1][1], map[i - 1][2]) + r;
		map[i][1] = min(map[i - 1][0], map[i - 1][2]) + g;
		map[i][2] = min(map[i - 1][0], map[i - 1][1]) + b;
	}
	cout << min(map[N][0], min(map[N][1], map[N][2])) << endl;

	return 0;
}