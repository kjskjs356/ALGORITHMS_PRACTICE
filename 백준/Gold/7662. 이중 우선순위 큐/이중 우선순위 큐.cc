#include <iostream>
#include <queue>
#include <map>
using namespace std;

#define endl '\n'

int T, k;
char cmd;
int n;
priority_queue<int, vector<int>, greater<int>> min_pq;
priority_queue<int, vector<int>, less<int>> max_pq;
map<int, int> chk;

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> T;
	while (T--) {
		while (!min_pq.empty()) min_pq.pop();
		while (!max_pq.empty()) max_pq.pop();
		chk.clear();
		cin >> k;
		while (k--) {
			cin >> cmd >> n;
			// 삽입
			if (cmd == 'I') {
				min_pq.push(n);
				max_pq.push(n);
				chk[n]++;
			}
			// 삭제
			else {
				// 원소개수 0이면 패스
				if (n == 1) {
					if (!max_pq.empty()) {
						chk[max_pq.top()]--;
						max_pq.pop();
					}
				}
				else {
					if (!min_pq.empty()) {
						chk[min_pq.top()]--;
						min_pq.pop();
					}
				}
				while (!min_pq.empty() && chk[min_pq.top()] == 0) min_pq.pop();
				while (!max_pq.empty() && chk[max_pq.top()] == 0) max_pq.pop();
			}
		}
		if (max_pq.empty() || min_pq.empty()) cout << "EMPTY" << endl;
		else cout << max_pq.top() << ' ' << min_pq.top() << endl;
	
	}

	return 0;
}