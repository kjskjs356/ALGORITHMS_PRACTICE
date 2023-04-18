#include <iostream>
#include <cmath>
using namespace std;

#define endl '\n'

long long a, b, c, k;

// 분할 정복
long long devide(long long b) {
	if (b == 0) return 1;
	if (b == 1) return a % c;

	k = devide(b / 2) % c;
	if (b % 2 == 0) return k * k % c;
	return k * k % c * a % c;
}

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> a >> b >> c;
	cout << devide(b);

	return 0;
}