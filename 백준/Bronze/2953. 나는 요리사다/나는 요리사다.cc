#include <iostream>

using namespace std;

int main() {
	int ans, total;
	ans = total = 0;
	for (int i = 0; i < 5; i++) {
		int temp_sum, a, b, c, d;
		cin >> a >> b >> c >> d;
		temp_sum = a + b + c + d;
		if (total < temp_sum) {
			ans = i + 1;
			total = temp_sum;
		}
	}
	cout << ans<<' '<<total << '\n';
}