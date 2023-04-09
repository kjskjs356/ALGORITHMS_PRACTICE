#include <iostream>
#include <queue>
using namespace std;
 
int N, X;
	queue<int> Q;
	string op;

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> N;
 
	for (int i = 0; i < N; i++) {
		cin >> op;
		if (op == "push") {
			cin >> X;
			Q.push(X);
		}
		else if (op == "pop") {
			if (Q.empty()) cout << -1 << '\n';
			else {
				cout << Q.front() << '\n';
				Q.pop();
			}
		}
		else if (op == "size") {
			cout << Q.size() << '\n';
		}
		else if (op == "empty") {
			cout << Q.empty() << '\n';
		}
		else if (op == "front") {
			if (Q.empty()) cout << -1 << '\n';
			else cout << Q.front() << '\n';
		}
		else if (op == "back") {
			if (Q.empty()) cout << -1 << '\n';
			else cout << Q.back() << '\n';
		}
	}
 
	return 0;
}