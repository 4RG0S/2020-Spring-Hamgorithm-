#include <iostream>
#include <string>

int main() {
	int N, count, title;
	std::cin >> N;
	// 0: 666, 1: 1666, ..., (6: 6660, 6+9: 6669), 6+10: 7666, 6+11: 8666, 9666, 10666, 11666, ... (16660, 
	// �׳� 666���� 1�� ���ذ��鼭 "666"�� ���ڿ��� ���Եȴٸ� count +1����
	for (int i = 666; ; i++) {
		std::string str;
		str = std::to_string(i);
		if (str.find("666") != std::string::npos) {
			count++;
		}
		if (count == N) {
			title = i;
			break;
		}
	}

	std::cout << title;

	return 0;
}