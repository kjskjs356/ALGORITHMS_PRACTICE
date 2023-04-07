#include <iostream>

#define endl "\n"
using namespace std;

int N, M, n;
int plus_arr[10000001] = { 0, };
int minus_arr[10000000] = { 0, };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	int num;
	for (int i = 0; i < N; ++i) {
		cin >> num;
		if (num >= 0) {
			plus_arr[num]++;
		}
		else {
			num *= -1;
			minus_arr[num]++;
		}
	}
	// 상근이꺼 체크
	cin >> M;
	while (M--) {
		cin >> n;
		if (n >= 0) {
			cout << plus_arr[n] << ' ';
		}
		else {
			n *= -1;
			cout << minus_arr[n] << ' ';
		}
	}
	

	return 0;
}