import pandas as pd
df=pd.read_csv("subbyte.csv")
def generateKeys(t,rcon,temp):
    o=[]
    p=[]
    for i in range(4):
        for j in range(4):
            if i==0 and j==0:
                p.append(hex(int(t[i][j],16)^int(rcon[j],16)^int(temp[j],16)).lstrip('0x')[-2:])
                if p[-1]=='':
                    p[-1]='00'
            else:
                p.append(hex(int(t[i][j],16)^int(temp[j],16)).lstrip('0x')[-2:])
                if p[-1]=='':
                    p[-1]='00'
        o.append(p)
        temp=p
        p=[]
    return o
key=input('enter 16 character key')
t=[]
for i in range(0,len(key),4):
    l=[]
    for j in range(4):
        l.append(hex(ord(key[i+j]))[2:])
    t.append(l)
temp1=t[-1][1:]+[t[-1][0]]
d={}
st='0123456789abcdef'
for i in range(len(st)):
    d[st[i]]=i
temp=[]
for i in temp1:
    temp.append(df.iloc[d[i[0]]][d[i[1]]])
rcon=['1','2','4','8','10','20','40','80','1b','36']
keys=[]
keys.append(t)
for i in range(10):
#     print(rcon[i])
    t=generateKeys(t,rcon[i],temp)
    keys.append(t)
#     print(t)
    temp1=t[-1][1:]+[t[-1][0]]
    temp=[]
    for j in temp1:
#         print(j)
        if len(j)==1:
            temp.append(df.iloc[0][d[j[0]]])
        else:
            temp.append(df.iloc[d[j[0]]][d[j[1]]])
    print(temp)
    print(t)
