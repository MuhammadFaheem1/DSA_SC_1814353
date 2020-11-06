a,b=map(int, input().split())

revA,revB=0, 0
while a and b!=0:
    A1=a % 10
    B1=b % 10
    revA = revA * 10 + A1
    revB = revB * 10 + B1
    a= a // 10
    b= b // 10

print(max(revA,revB))
