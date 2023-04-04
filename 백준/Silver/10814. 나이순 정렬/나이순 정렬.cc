#include <iostream>
#include <vector>
#include <queue>

#define endl "\n"
using namespace std;

int N;
int age;
string name;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	int x;
	string y;
	priority_queue < pair<pair<int, int>, string>, vector<pair<pair<int, int>, string>>, greater<pair<pair<int, int>, string>>> pq;
	for (int i = 0; i < N; ++i) {
		cin >> x >> y;
		pq.push({ {x, i}, y });
	}
	while (!pq.empty()) {
		age = pq.top().first.first;
		name = pq.top().second;
		pq.pop();
		cout << age << ' ' << name << endl;
	}

	return 0;
}