a=int(input())
for i in range(2,a+1):
  if a%i==0:
    break;
if(i==a):
  print("yes")
else:
  print("no")
