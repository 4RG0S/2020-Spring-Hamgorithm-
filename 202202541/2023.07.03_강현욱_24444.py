from collections import deque
x, y, z = map(int, input().split())
#�Է� ���� ����
visit=[0]*(x+1)
#�湮�� false ����
nod=[[] for k in range(x+1)]
for o in range(y):
    i,j = map(int, input().split())
    nod[i].append(j)
    nod[j].append(i)
for i in range(1,x+1):
    nod[i].sort()
cnt=1
visit[z]=1
q=deque([z])
while q:
    v=q.popleft()
    for i in nod[v]:
        if visit[i]>0:
            continue
        cnt+=1
        visit[i]=cnt
        q.append(i)

for i in range(1,x+1):
    print(visit[i])