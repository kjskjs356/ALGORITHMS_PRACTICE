#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
	int N, M, ans;
	ans = 0;
	cin >> N >> M;
	unordered_map<string, int> word_list;
	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		word_list[word] = 1;
	}
	for (int i = 0; i < M; i++) {
		string word;
		cin >> word;
		auto item = word_list.find(word);
		if (item != word_list.end()) ans += 1;
	}
	cout << ans;
}