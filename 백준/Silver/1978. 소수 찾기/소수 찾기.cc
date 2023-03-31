#include <iostream>
#include <vector>

#define endl "\n"
using namespace std;

int N, ans;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	ans = 0;
	cin >> N;
	while (N--) {
		int num;
		bool flag = true;
		cin >> num;
		if (num == 1) continue;
		for (int i = 1; i <= num; ++i) {
			if (num % i == 0) {
				if (!(i == 1 || i == num)) {
					flag = false;
				}
			}
		}
		if (flag) ++ans;
	}
	cout << ans;

	return 0;
}