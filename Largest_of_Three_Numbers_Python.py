# largest of three numbers
a,b,c=input().split(",")
a=float(a)
b=float(b)
c=float(c)
if a>b:
   if a>c:
      print(a)
   else:
      print(c)
elif b>a:
   if b>c:
      print(b)
   else:
      print(c)
elif c>a:
   if c>b:
      print(c)
   else:
      print(b)


