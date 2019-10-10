def palindrome(i):
  a,palin=i,0
  while(a!=0):
    b=a%10
    a=a//10
    palin=palin*10+b
  return palin  

def base(i,base_value):
  d,t=i,0
  while(d!=0):
      e=d%base_value
      d=d//base_value
      t=t*10+e
  return t  
    



number,base_value=map(int,input().split())
Sum=0
for num in range(1,number+1):
  c=palindrome(num)
  if num==c and num%base_value!=0:
      f=base(num,base_value)
      g=palindrome(f)
      if f==g:
        Sum=Sum+num
print(Sum)      
