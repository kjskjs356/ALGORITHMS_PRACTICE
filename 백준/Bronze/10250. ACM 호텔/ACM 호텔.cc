#include <iostream>

#define endl '\n'
using namespace std;

int main() {
	int T;
	int H, W, N;
	int ans;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> H >> W >> N;

		if (N % H == 0) {
			ans = H * 100 + (N / H);
		}
		else {
			ans = (N % H) * 100 + (N / H) + 1;
		}
		cout << ans << endl;
	}
}