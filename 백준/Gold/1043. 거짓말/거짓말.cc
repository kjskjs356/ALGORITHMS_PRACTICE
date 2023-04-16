#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

#define endl '\n'

int N, M, num, number, ans;
int p, person;
bool check;
bool chk_party[50];
set<int> true_person;
vector<int> party[50];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;
	cin >> num;
	for (int i = 0; i < num; ++i) {
		cin >> number;
		true_person.insert(number);
	}
	for (int i = 0; i < M; ++i ) {
		cin >> p;
		for (int j = 0; j < p; ++j) {
			cin >> person;
			party[i].push_back(person);
		}
	}

	// 각 파티마다 진실아는 사람 모두 발견할때까지 탐색
	while (true) {
		check = false;
		// 파티 순회
		for (int i = 0; i < M; ++i) {
			for (int j:true_person) {
				// 파티 안에 진실을 아는 사람이 존재하면 해당 파티 모두가 진실을 알게됨
				if (find(party[i].begin(), party[i].end(), j) != party[i].end()) {
					chk_party[i] = true;
					// 파티에 있는 사람들을 true_person에 추가
					for (int k :party[i]) {
						if (true_person.find(k) == true_person.end()) {
							check = true;
							true_person.insert(k);
						}
					}
				}
			}
		}
		
		if (!check) break;
	}
	// 거짓말한 파티 수 계산
	for (int i = 0; i < M; ++i) {
		if (!chk_party[i]) ++ans;
	}
	cout << ans;

	return 0;
}