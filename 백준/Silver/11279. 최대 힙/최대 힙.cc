#include <iostream>
#include <queue>

using namespace std;

#define endl '\n'

int N, num;
priority_queue<int> pq;

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	while (N--) {
		// 0이 입력되면 큰 수 출력 or 비어있으면 0 출력
		cin >> num;
		if (num == 0) if (pq.empty()) cout << 0 << endl;
		else {
			cout << pq.top() << endl;
			pq.pop();
		}
		else pq.push(num);
	}

	return 0;
}