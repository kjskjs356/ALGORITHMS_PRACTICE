#include <iostream>
#include <cmath>

using namespace std;

#define endl '\n'

int N, r, c;
int ans;

void recursion(int x, int y, int n) {
	if (r == x && c == y) {
		cout << ans << endl;
		return;
	}
	// 큰 사각형부터 r, c에 일치할때까지 축소하기
	if (r >= x && r < x + n && c >= y && c < y + n) {
		// 1사분면
		recursion(x, y, n / 2);
		// 2사분면
		recursion(x, y + n / 2, n / 2);
		// 3사분면
		recursion(x + n / 2, y, n / 2);
		// 4사분면
		recursion(x + n / 2, y + n / 2, n / 2);
	}
	else {
		ans += n * n;
	}

}

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> r >> c;

	recursion(0, 0, pow(2, N));
	
	return 0;
}