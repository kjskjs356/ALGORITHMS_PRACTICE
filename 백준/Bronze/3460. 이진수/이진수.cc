#include <iostream>
#include <vector>

#define endl "\n"
using namespace std;

int T, n;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> T;
	while (T--) {
		vector<int> arr;
		cin >> n;
		while (n > 0) {
			if (n % 2 == 0) arr.push_back(0);
			else arr.push_back(1);
			n /= 2;
		}
		for (int i = 0; i < arr.size(); ++i) {
			if (arr[i] == 1) cout << i << ' ';
		}
		cout << endl;
	}
	return 0;
}