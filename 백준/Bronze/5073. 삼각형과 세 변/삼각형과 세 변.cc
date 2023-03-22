#include <iostream>
#include <deque>

using namespace std;

int x, y, z;

int main() {
	while (1) {
		cin >> x >> y >> z;
		if (x == 0 && y == 0 && z == 0) break;
		if (x + y <= z || y + z <= x || x + z <= y) cout << "Invalid" << '\n';
		else if (x != y && y != z && z != x) cout << "Scalene" << '\n';
		else if (x == y && y != z || y == z && z != x || x == z && y != z) cout << "Isosceles" << '\n';
		else if (x == y && y == z && z == x) cout << "Equilateral" << '\n';
		else cout << "Scalene" << '\n';
	};
	return 0;
}