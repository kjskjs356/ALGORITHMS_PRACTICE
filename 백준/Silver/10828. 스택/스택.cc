#include <iostream>
#include <vector>

using namespace std;

#define endl '\n'

int N, num;
string cmd;
vector<int> stack;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N;
	while (N--) {
		cin >> cmd;
		if (cmd == "push") {
			cin >> num;
			stack.push_back(num);
		}
		else if (cmd == "pop") {
			if (stack.empty()) cout << -1 << endl;
			else {
				int last = stack.back();
				cout << last << endl;
				stack.pop_back();
			}
		}
		else if (cmd == "size") {
			cout << stack.size() << endl;
		}
		else if (cmd == "empty") {
			if (stack.empty()) cout << 1 << endl;
			else cout << 0 << endl;
		}
		else if (cmd == "top") {
			if (stack.empty()) cout << -1 << endl;
			else cout << stack.back() << endl;
		}
	}
	return 0;
}