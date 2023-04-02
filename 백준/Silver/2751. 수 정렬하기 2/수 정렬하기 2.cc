#include <iostream>
#include <vector>
using namespace std;

#define endl '\n'

int N;
int plus_arr[1000001];
int minus_arr[1000001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N;
	while (N--) {
		int num;
		cin >> num;
		if (num >= 0) plus_arr[num] = 1;
		else minus_arr[num * (-1)] = 1;
	}
	for (int i = 1000000; i > 0;--i) {
		if (minus_arr[i] == 1) cout << (-1) * i << endl;
	}
	for (int i = 0; i <= 1000000;++i) {
		if (plus_arr[i] == 1) cout << i << endl;
	}

	return 0;
}