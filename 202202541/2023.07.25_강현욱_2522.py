from collections import deque
import sys
input=sys.stdin.readline
member, nod= map(int, input().split())
member_list=[[] for i in range(member+1)]
#Ž����屸��
enter_case=[0]*(member+1)
#Ž�� ��忬�� ����
for _ in range(nod):
    x,y=map(int, input().split())
    member_list[x].append(y)
    enter_case[y]+=1
#��� �Է�
result=[]
q=deque()
for j in range(1,member+1):
    if(enter_case[j]==0):
        q.append(j)
while q:
    now=q.popleft()
    result.append(now)
    for w in member_list[now]:
        enter_case[w]-=1
        if enter_case[w]==0:
            q.append(w)
#��������
for j in range(0,len(result)):
    print("%d "%(result[j]),end='')
