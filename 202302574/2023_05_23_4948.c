#include<stdio.h>
int main() {
    int n, i, j, cnt = 0;
    int to = 250000;
    int arr[250000] = { 0, };

    //1. �迭 ���� �� ���� 1�� �ʱ�ȭ
    for (i = 2; i <= to; i++) {
        arr[i] = 1;
    }
    //2. i�� �Ҽ��� ����, i�� ���(�ڱ� �ڽ��� ����)�� ���������� ���
    for (i = 2; i <= to; i++) {
        if (arr[i] == 0) continue;
        //i�� �Ҽ��� �ƴ� ��, continue
        //��, i�� �Ҽ��� ����, ������ ��ɹ� ����
        for (j = 2 * i; j <= to; j += i) {
            arr[j] = 0;
        }
    }
    while (1) {
        scanf("%d", &n);
        if (n == 0) break;

        cnt = 0;
        for (i = n+1; i <= 2 * n; i++) {
            if (arr[i] == 1) cnt++;
        }
        printf("%d\n", cnt);
    }
}