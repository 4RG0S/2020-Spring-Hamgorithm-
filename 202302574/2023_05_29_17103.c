#include<stdio.h>
#define to 1000000
int main() {
    int N, cnt, num, i, j;
    int arr[1000000] = { 0, };

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
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        cnt = 0;
        scanf("%d", &N);
        for (int j = 1; j <= N / 2; j++) {
            cnt += arr[j] && arr[N - j];
        }
        printf("%d\n", cnt);
    }
}