import random
from typing import NamedTuple

class Player: 
  def __init__(self, name, xeri,sum,ace):
      self.name=name
      self.xeri =[]
      self.sum= sum
      self.ace= ace
xartia=[]

range1=[i for i in range(1,11)]
symbola=["J","Q","K"]
xrwmata=("spade","heart","tile","clover")

for i in range1+symbola: 
  for j in xrwmata:
   xartia.append([i,j])

def cfc(xartia):
  
  global top
  if top>51:
   top=0

   random.shuffle(xartia) 
   print("----NEW CARD DECK---")
   
  
def xer(named,k):
  print(named,"`S HAND WAS ") 
  for row in range(0,len(k)): print(k[row])
  print(k)
  
   


 
random.shuffle(xartia)
random.shuffle(xartia)
random.shuffle(xartia)
#print(xartia)

run=True

print("Give me your username:")
p1= Player(input(),xartia,0,0)
p2= Player("pc",xartia,0,0)
global top
top=0



while(True):
 
 for i in range(2):
  p1.xeri.append(xartia[top]) 
  top=top+1
  cfc(xartia)
  
  
  if p1.xeri[i][0]=="J" or p1.xeri[i][0]=="Q" or p1.xeri[i][0]=="K":
   p1.sum+=10
  elif p1.xeri[i][0]==1:
    p1.ace=True
    if p1.sum+11>21:
     p1.sum=p1.sum+1
    else:
     p1.sum=p1.sum+11
  else:
   p1.sum=p1.sum + p1.xeri[i][0]
  print(p1.name,"`S HAND`S SUM WAS ",p1.sum,"ON HAND:",p1.xeri[i][0],p1.xeri[i][1])
 
 for i in range(2):
  p2.xeri.append(xartia[top]) 
  top=top+1
  
  cfc(xartia)
  
  
  if p2.xeri[i][0]=="J" or p2.xeri[i][0]=="Q" or p2.xeri[i][0]=="K":
   p2.sum+=10
  elif p2.xeri[i][0]==1:
    p2.ace=True
    if p2.sum+11>21:
     p2.sum=p2.sum+1
    else:
     p2.sum=p2.sum+11  
  else:
   p2.sum=p2.sum + p2.xeri[i][0]
 
 print("AI`S HAND:",p2.xeri[0][0],p2.xeri[0][1])
 
 
 while(True):
  print("HIT OR PASS","SUM:",p1.sum) 
  if p1.sum==21 or p2.sum==21:
    break
  choice=input()
  if choice=="HIT" or choice=="H" or choice=="h" :
   p1.xeri.append(xartia[top]) 
   print(xartia[top])
   top=top+1
   
   cfc(xartia)
   
   if p1.xeri[len(p1.xeri)-1][0]=="J" or p1.xeri[len(p1.xeri)-1][0]=="Q" or p1.xeri[len(p1.xeri)-1][0]=="K":
    p1.sum+=10
   elif p1.xeri[len(p1.xeri)-1][0]==1:
    
    if p1.sum+11>21:
     p1.sum=p1.sum+1
    else:
     p1.sum=p1.sum+11
     p1.ace=p1.ace+1
   else:
    p1.sum=p1.sum+p1.xeri[len(p1.xeri)-1][0]
   
   if p1.sum>=21:
     if p1.ace==0:
      break
     else:
      p1.sum=p1.sum-10
      p1.ace=p1.ace-1
   
   
  elif choice=="PASS" or choice=="P" or choice=="p" :
   print("PASSED")
   break
 
 while(p2.sum<17):
  
  p2.xeri.append(xartia[top]) 
  top=top+1
  
  if p2.xeri[len(p2.xeri)-1][0]=="J" or p2.xeri[len(p2.xeri)-1][0]=="Q" or p2.xeri[len(p2.xeri)-1][0]=="K":
   p2.sum+=10
  elif p2.xeri[len(p2.xeri)-1][0]==1:
     
   if p2.sum+11>21:
    p2.sum=p2.sum+1
   else:
    p2.sum=p2.sum+11
    p2.ace=p2.ace+1
  
  else:
    p2.sum=p2.sum + p2.xeri[len(p2.xeri)-1][0] 
  
  while(p2.sum>21):
    if p2.ace>0:
     p2.sum=p2.sum-10
     p2.ace=p2.ace-1
    else:
     break
  
  cfc(xartia)
 
 
 


 
 
 
 if p1.sum==21:
    print("Blackjack:",p1.name)
    
 
 if p2.sum==21:
    print("Blackjack:",p2.name)
    

 if p1.sum<=21 and p2.sum<=21:
  if p1.sum>p2.sum:
   print("YOU WON. ")
   xer(p1.name,p1.xeri)
   xer(p2.name,p2.xeri)
  else:
   print("YOU LOST. ")
   xer(p1.name,p1.xeri)
   xer(p2.name,p2.xeri)
 elif p1.sum>21:
  if p2.sum<=21:
   print("YOU LOST BECAUSE YOUR HAND`S SUM WAS OVER 21")
   xer(p1.name,p1.xeri)
   xer(p2.name,p2.xeri)
  else:
   print("BOTH PLAYERS LOST")
   xer(p1.name,p1.xeri)
   xer(p2.name,p2.xeri)
 else:
  if p1.sum<=21:
   print("YOU WON. ")
   xer(p1.name,p1.xeri)
   xer(p2.name,p2.xeri)
  
 p1.sum=0
 p2.sum=0
 p1.xeri.clear()
 p2.xeri.clear()

 
 


 
