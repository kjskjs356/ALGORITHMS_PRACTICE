#include <iostream>

using namespace std;

int main() {
	int ans, temp, up, down;
	ans = 0;
	temp = 0;
	for (int i = 0; i < 10; i++) {
		cin >> down >> up;
		temp += up;
		temp -= down;
		if (ans < temp) {
			ans = temp;
		}
	}
	cout << ans << "\n";
}