#include <iostream>
#include <vector>
using namespace std;

#define endl '\n'

int T, num;
vector<int> dp;;


int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> T;
	while (T--) {
		dp.clear();
		dp.push_back(0);
		dp.push_back(1);
		cin >> num;
		if (num == 0) {
			cout << 1 << ' ' << 0 << endl;
			continue;
		}
		else {
			for (int i = 1; i <= num;++i) {
				dp.push_back(dp[i] + dp[i - 1]);
			}
		}
		cout << dp[num - 1] << ' ' << dp[num] << endl;
	}

	return 0;
}