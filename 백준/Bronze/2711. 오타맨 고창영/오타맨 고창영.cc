#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int idx;
		string arr;
		cin >> idx >> arr;
		idx -= 1;
		string ans;
		for (int j = 0; j < arr.length(); j++) {
			if (idx == j) {
				continue;
			}
			else {
				ans += arr[j];
			}
		}
		cout << ans << '\n';
	}
}