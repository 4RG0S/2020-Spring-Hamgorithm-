import heapq
import sys
input=sys.stdin.readline
heap=[]
x=int(input())
for i in range(x):
    y=int(input())
    heapq.heappush(heap,y)
    #heap �߰�
    if(y==0):
        heapq.heappop(heap)
        # �Է°�
        if(len(heap)==0):
            print(0)
        else:
            print(heapq.heappop(heap))
        
    
