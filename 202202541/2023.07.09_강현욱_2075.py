import heapq
import sys
input=sys.stdin.readline
x=int(input())
heap=[]
z=[]
for k in range(x):
     z=list(map(int,input().split()))
     for j in z:
          if len(heap)<x:
               heapq.heappush(heap,j)
               #x���� ������ �̹Ƿ� x������ ����
          else:
               if(heap[0]<j):
                    heapq.heappop(heap)
                    heapq.heappush(heap,j)
                #x���� ū �� ���ؼ� �߰�
print(heapq.heappop(heap))
    #���������� n������
                    


            
        


