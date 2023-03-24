#include <iostream>
#include <algorithm>
#include <vector>

#define endl "\n"
using namespace std;

int N, ans;
vector<int> arr = { 0, 1, 2, 3, 4, 5, 6, 7, 8};
int inning[50][9];


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> inning[i][j];
		}
	}
	do {
		int seq[9];
		bool breaker = false;
		for (int i = 0, j = 0; i < 9; i++, j++) {
			// 1번 선수가 4번타자가 아닌 경우의 수는 패스
			if (j == 0 && arr[i] != 3) {
				breaker = true;
				break;
			}
			seq[j] = arr[i];
		}
		if (breaker) continue;
		// 1이닝씩 진행, 아웃이 3개 될때마다 다음 이닝으로 넘어감
		int cnt, out_cnt, score;
		cnt = 0;
		out_cnt = 0;
		score = 0;
		// 선수들의 진출상태
		int now[9] = { 0, };
		// 다음 진출 선수
		int number = 0;
		while (cnt < N) {
			auto it  = find(begin(seq), end(seq), number);
			int idx = distance(seq, it);
			number++;
			if (number == 9) number = 0;
			// 아웃인 경우 1스택 추가
			if (inning[cnt][idx] == 0) {
				out_cnt += 1;
				// 3아웃은 다음이닝
				if (out_cnt == 3) {
					cnt++;
					out_cnt = 0;
					for (int i = 0; i < 9; i++) now[i] = 0;
					continue;
				}
			}
			else {
				// 진출해있는 선수들 먼저 진루하고 타자 진루
				for (int j = 0; j < 9; j++) {
					if (now[j] != 0) now[j] += inning[cnt][idx];
					if (now[j] > 3) {
						now[j] = 0;
						score += 1;
					}
				}
				now[idx] += inning[cnt][idx];
				if (now[idx] > 3) {
					now[idx] = 0;
					score+= 1;
				}
			}
		}
		ans = max(ans, score);
	} while (next_permutation(arr.begin(), arr.end()));
	cout << ans;
	return 0;
}
