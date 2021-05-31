def wallis(n):
  pi=1
  for i in range(1,n):
    pi=pi*(4*(i**2)/(4*(i**2)-1))
  pi=pi*2
  return pi

import random
def monte_carlo(n):
  cir=0
  sq=0
  for i in range(1,n):
    x=random.random()
    y=random.random()
    if (x**2 + y**2)<=1:
      cir+=1
      sq+=1
    else:
      sq+=1 
  pi=4*(cir/sq) 
  return pi

def main():
  print("Enter no of itteration required(value of n)")
  i=int(input())
  i=wallis(i)
  print("Pi value from wallis is",i)
  print("Enter no of drats used(value of n)")
  j=int(input())
  j=monte_carlo(j)
  print("Pi value from monte carlo is",j)
if __name__=="__main__":
  main()


