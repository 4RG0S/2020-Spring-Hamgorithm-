import sys
input=sys.stdin.readline
x,y=map(int,input().split())
ls=[]
ls=list(map(int, input().split()))
start=0
end=0
sum=0
lth=[]
#�������� Ȱ��
for start in range(x):
    while sum<y and end<x:
        sum+=ls[end]
        end+=1
    if(sum>=y):
        lth.append(end-start)
        #���� �߰��ؼ� ������ ���
    sum=sum-ls[start]
lth.sort()
#�ش��ϴ°� ���ٸ� lth ����Ʈ ���̰� 0��``
if(len(lth)==0):
    print(0)
else:
    print(lth[0])


