import heapq
import sys
input=sys.stdin.readline
heap=[]
x=int(input())
for i in range(x):
    y=int(input())

    if(y==0):
        # �Է°� 0�̸� ������Ʈ�� �߰� ����
        if(len(heap)==0):
            print(0)
        else:
            print(-heapq.heappop(heap))
            #���� ��� �ؼ� ���� �޸� �ִ밪
    else:
        heapq.heappush(heap,-y)
        #���� ����
    
