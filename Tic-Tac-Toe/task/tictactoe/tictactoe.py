amit =input();
amit=list(amit)
k=0;
for i in range(0,9):
    print("-",end='')
print()
for j  in range(0,15):
    if(j==0 or j==5 or j==10):
        print("|",end=' ');
    elif(j==4 or j==9 or j==14):
        print("|");
    else:
        print(amit[k],end=' ')
        k=k+1
for l in range(0,9):
    print("-",end='')