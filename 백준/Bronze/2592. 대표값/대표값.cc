#include <iostream>

using namespace std;

int main() {
	int a[10];
	int arr[1001]{ 0 };
	int a_sum, avg, ans, cnt;
	a_sum = 0;
	for (int i = 0; i < 10; i++) {
		cin >> a[i];
		a_sum += a[i];
		arr[a[i]] += 1;
	}
	avg = a_sum / 10;
	cout << avg << "\n";
	ans = 0;
	cnt = 0;
	for (int i = 0; i <= 1000; i += 10) {
		if (cnt < arr[i]) {
			ans = i;
			cnt = arr[i];
		}
	}
	cout << ans << "\n";
}