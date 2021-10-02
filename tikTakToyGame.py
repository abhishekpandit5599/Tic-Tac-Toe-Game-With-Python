# Screen Display Function 
def screen (l):
  print  ("***********________GAME________**********\n")
  print  (f"                |       |          ")
  print  (f"            {l[0]}   |   {l[1]}   |   {l [2]}   ")
  print  (f"         _______|_______|_______   ")
  print  (f"                |       |          ")
  print  (f"            {l[3]}   |   {l[4]}   |   {l [5]}   ")
  print  (f"         _______|_______|_______   ")
  print  (f"                |       |          ")
  print  (f"            {l[6]}   |   {l[7]}   |   {l [8]}   ")
  print  (f"                |       |          ")
  print  ("\n****************************************")
  print  ("First Player Symbol (X)")
  print  ("Second Player Symbol (0)")
  print  ("****************************************\n")

# Player 1 Input 
def player1 (l):
  k = 0
  play1 = int (input ("Enter the First Player :->"))
  k = exChange1 (l, play1)
  if k == 0:
    return 0
  return 1
  
  
# Player 1 Exchange 'X'  
def exChange1 (l, play1):
  if l [play1-1] != '0' and l [play1-1] != 'X':
    l [play1-1] = 'X'
  
  else:
    print  ("\n****************************************")
    print  ("Invalid Space Please Try Again :")
    print  ("****************************************\n")
    player1 (l)
  screen (l)
    
  if(((l[0]=='X')and(l[4]=='X')and(l[8]=='X'))or
   ((l[2]=='X')and(l[4]=='X')and(l[6]=='X'))or
   ((l[0]=='X')and(l[1]=='X')and(l[2]=='X'))or
   ((l[3]=='X')and(l[4]=='X')and(l[5]=='X'))or
   ((l[6]=='X')and(l[7]=='X')and(l[8]=='X'))or
   ((l[0]=='X')and(l[3]=='X')and(l[6]=='X'))or
   ((l[1]=='X')and(l[4]=='X')and(l[7]=='X'))or
   ((l[2]=='X')and(l[5]=='X')and(l[8]=='X'))):
     print  ("\n****************************************")
     print  ("First Player is Winner")
     print  ("****************************************\n")
     return 1
  
  li = ['X','0']
  if ((l [0] in li) and (l [1] in li) and (l [2] in li)and
     (l [3] in li) and (l [4] in li) and (l [5] in li )and
     (l [6] in li) and (l [7] in li) and (l [8] in li)):
  
    print  ("\n****************************************")
    print  ("Game Draw")
    print  ("****************************************\n")
    return 1  
  return 0 
  

# Player 2 Input  
def player2 (l):
  j = 0
  play2 = int (input ("Enter the Second Player :->"))
  j = exChange2 (l, play2)
  if j == 0:
    return 0
  return 1
  
  
# Player 2 Exchange '0'  
def exChange2 (l, play2):
  if l [play2-1] != 'X' and l [play2-1] != '0':
    l [play2-1] = '0'
  
  else:
    print  ("\n****************************************")
    print  ("Invalid Space Please Try Again :")
    print  ("****************************************\n")
    player2 (l)
  screen (l)
  
  if(((l[0]=='0')and(l[4]=='0')and(l[8]=='0'))or
   ((l[2]=='0')and(l[4]=='0')and(l[6]=='0'))or
   ((l[0]=='0')and(l[1]=='0')and(l[2]=='0'))or
   ((l[3]=='0')and(l[4]=='0')and(l[5]=='0'))or
   ((l[6]=='0')and(l[7]=='0')and(l[8]=='0'))or
   ((l[0]=='0')and(l[3]=='0')and(l[6]=='0'))or
   ((l[1]=='0')and(l[4]=='0')and(l[7]=='0'))or
   ((l[2]=='0')and(l[5]=='0')and(l[8]=='0'))):
     print  ("\n****************************************")
     print  ("Second Player is Winner")
     print  ("****************************************\n")
     return 1
  return 0


# Run Game
def Run ():
  l = [1,2,3,4,5,6,7,8,9]  
  i = 0
  screen (l)
  while i==0:
    i = player1 (l)
    if i==1:
      break
    i = player2 (l)



# Main
Run () 
choice = 'y'
while choice == 'y' or choice == 'Y' :
  choice = input ("Play Again Y/N :-> ")
  if choice == 'y' or choice == 'Y' :
    Run ()
   
