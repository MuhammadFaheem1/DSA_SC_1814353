pos=1
swap=input()
size=len(swap)
for i in range(size):
    if swap[i]=='A':
        if pos==1:
            pos=2
        elif pos==2:
            pos=1
    elif swap[i]=='B':
        if pos==2:
            pos=3
        elif pos==3:
            pos=2
    elif swap[i]=='C':
        if pos==1:
            pos=3
        elif pos==3:
            pos=1

print(pos)
