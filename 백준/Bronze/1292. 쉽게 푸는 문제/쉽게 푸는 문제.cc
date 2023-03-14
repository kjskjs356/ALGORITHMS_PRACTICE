#include <iostream>

using namespace std;

int main() {
	int start, end, ans, idx, cnt;
	cin >> start >> end;
	start -= 1;
	ans = 0;
	idx = 0;
	cnt = 1;
	while (idx < end) {
		for (int i = 0; i < cnt; i++) {
			if (idx >= start) ans += cnt;
			idx += 1;
			if (idx == end) break;
		}
		cnt += 1;
	}
	cout << ans;
}