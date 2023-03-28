#include <iostream>
#include <algorithm>
#include <vector>

#define endl "\n"
using namespace std;

int M;
vector<int> arr;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> M;
	for (int i = 0; i < M; i++) {
		string cmd; 
		int num;
		cin >> cmd;
		if (cmd == "add") {
			cin >> num;
			bool exist = false;
			for (int j = 0; j < arr.size(); j++) {
				if (arr[j] == num) {
					exist = true;
					break;
				}
			}
			if (!exist) arr.push_back(num);
		}
		else if (cmd == "remove") {
			cin >> num;
			arr.erase(remove(arr.begin(), arr.end(), num), arr.end());
		}
		else if (cmd == "check") {
			cin >> num;
			bool exist = false;
			for (int j = 0; j < arr.size(); j++) {
				if (arr[j] == num) {
					cout << 1 << endl;
					exist = true;
					break;
				}
			}
			if (exist) continue;
			else cout << 0 << endl;
		}
		else if (cmd == "toggle") {
			cin >> num;
			bool exist = false;
			for (int j = 0; j < arr.size(); j++) {
				if (arr[j] == num) {
					exist = true;
					break;
				}
			}
			if (exist) arr.erase(remove(arr.begin(), arr.end(), num), arr.end());
			else arr.push_back(num);
		}
		else if (cmd == "all") {
			arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 };
		}
		else if (cmd == "empty") arr = {};
	}
	return 0;
}