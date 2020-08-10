A=input()
B=input()
C=A.split()
D=B.split()
nA=0
nB=0
if(len(C)==3 and len(D)==3):
    for i in range(3):
        if(((int (C[i]))<(int (D[i]))) and ((int (D[i]))<100)):
            nB+=1
        elif(((int (C[i]))>(int (D[i]))) and ((int (C[i]))<100)):
            nA+=1
print(nA,nB)
