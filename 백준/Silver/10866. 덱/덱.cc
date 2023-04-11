#include <iostream>
#include <deque>
using namespace std;

#define endl '\n'

int N, m, x;
deque<int> dq;
string op;

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	while (N--) {
		cin >> op;
		if (op == "push_back") {
			cin >> m;
			dq.push_back(m);
		}
		else if (op == "push_front") {
			cin >> m;
			dq.push_front(m);
		}
		else if (op == "pop_front") {
			if (dq.empty()) cout << -1 << endl;
			else {
				x = dq.front();
				cout << x << endl;
				dq.pop_front();
			}
		}
		else if (op == "pop_back") {
			if (dq.empty()) cout << -1 << endl;
			else {
				x = dq.back();
				cout << x << endl;
				dq.pop_back();
			}
		}
		else if (op == "size") cout << dq.size() << endl;
		else if (op == "empty") cout << dq.empty() << endl;
		else if (op == "front") {
			if (dq.empty()) cout << -1 << endl;
			else cout << dq.front() << endl;
		}
		else if (op == "back") {
			if (dq.empty()) cout << -1 << endl;
			else cout << dq.back() << endl;
		}
	}
	return 0;
}