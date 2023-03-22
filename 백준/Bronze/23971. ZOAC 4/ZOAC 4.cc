#include <iostream>
#include <deque>

using namespace std;

int H, W, N, M;

int main() {
	cin >> H >> W >> N >> M;
	int row, col;
	row = H / (N + 1);
	if (H % (N + 1) > 0) row += 1;
	col = W / (M + 1);
	if (W % (M + 1) > 0) col += 1;
	cout << row * col;
}