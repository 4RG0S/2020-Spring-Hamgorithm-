x,y = map(int, input().split())
ls=[]
for _  in range(x):
    ls.append(int(input()))
ls.sort()
#�������;����� �����ϴ°� ���Ѱǰ���?
start=0
end=1
rs=0
sub=0
while True:
    if(start==x or end==x):
        break
        #st���� ������ ���ų� end�� ������ ���� �극��ũ
    sub=ls[end]-ls[start]
    if(sub>y):
         start+=1
         if(sub<=rs or rs==0):
                rs=sub
    elif(sub<y):
        end+=1
    elif(sub==y):
        rs=sub
        break
print(rs)




    


