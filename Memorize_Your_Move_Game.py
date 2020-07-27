Game_dict={'Easy':{'Size':10, 'Life':5, 'Jump':5, 'Obstacle':10, 'Advantage':20,
                   'Obstacle_coordinates':[[3, 4],[ 4, 6], [6, 0], [7, 1], [8, 1], [7, 3], [1, 0], [8, 0], [9, 2], [2, 9]],

                   'Advantage_coordinates':[[5, 6], [7, 2], [7, 4], [1, 0], [6, 5], [1, 0], [2, 4], [6, 6], [2, 3], [4, 9],
                                            [3, 2], [0, 9], [0, 7], [1, 5], [7, 0], [9, 5],[4, 4], [3, 8], [3, 5], [5, 3]]},

           'Medium':{'Size':20, 'Life':8, 'Jump':10,'Obstacle':15, 'Advantage':25,
                     'Obstacle_coordinates':[[19, 20], [6, 16], [16, 6], [4, 4], [12, 6], [15, 10], [18, 10], [11, 9], [15, 17], [15, 9], [3, 1], [2, 16],
                                             [19, 17], [3, 2],[0, 3]],

                     'Advantage_coordinates': [[8, 8], [13, 15], [2, 8], [2, 12], [1, 4], [13, 5], [6, 3], [8, 5], [15, 12], [14, 7],[2, 5], [9, 13], [5, 10],
                                               [15, 8], [1, 4],[ 15, 11],[9, 12], [3, 11], [5, 14], [6, 13], [14, 16], [8, 3], [4, 17], [10, 11], [7, 11]]},

           'Hard':{'Size':25, 'Life':10, 'Jump':15, 'Obstacle':20, 'Advantage':35,
                   'Obstacle_coordinates':[[10, 19],[ 5, 5],[ 18, 6],[ 16, 8], [13, 19], [19, 12], [15, 4], [16, 15], [1, 8], [8, 13], [14, 20], [17, 18],
                                            [1, 9], [7, 19], [3, 1], [10, 7], [6, 1], [4, 5], [3, 10], [11, 4]],

                   'Advantage_coordinates':[[2, 16], [6, 17], [9, 12], [18, 18], [12, 6], [4, 2], [1, 1], [18, 12], [11, 14], [12, 9], [17, 2], [19, 0], [16, 13], [0, 7],
                                            [12, 0], [8, 15], [11, 3], [4, 16], [13, 16], [5, 19], [9, 1], [6, 18], [8, 7], [7, 17], [3, 1], [6, 18], [12, 1], [19, 1], [5, 2],
                                            [9, 3], [9, 19], [16, 12], [3, 13], [3, 13], [5, 2]] }}

def Game_State_Sign(x,y,level):
  Obstacle_list = Game_dict[level]['Obstacle_coordinates']
  Advantage_list = Game_dict[level]['Advantage_coordinates']
  size = Game_dict[level]['Size']
  for i in range(0, size):
    for j in range(0, size):
      list_ij=[i,j]
      if (i==x and j==y):
        print("s",end=' ')
      elif (list_ij in Obstacle_list):
        print("*",end=' ')
      elif (list_ij in Advantage_list):
        print("+",end=' ')
      elif (i==(size-1) and j==(size-1)):
        print("e",end=' ')
      else:
        print("-",end=' ')
    print('\n')

def Game_State_Coordinate(x,y,level):
  Obstacle_list = Game_dict[level]['Obstacle_coordinates']
  Advantage_list = Game_dict[level]['Advantage_coordinates']
  size = Game_dict[level]['Size']
  for i in range(0, size):
    for j in range(0, size):
      list_ij=[i,j]
      if (i==x and j==y):
        print("\033[0;37;44m {:2.0f},".format(i),j,end='  ')
      elif (list_ij in Obstacle_list):
        print("\033[0;37;41m {:2.0f},".format(i),j,end='  ')
      elif (list_ij in Advantage_list):
        print("\033[0;37;42m {:2.0f},".format(i),j,end='  ')
      elif i==(size-1) and j==(size-1):
        print("\033[0;37;45m {:2.0f},".format(i),j,end='  ')
      else:
        print("\033[0;30;47m {:2.0f},".format(i),j,end='  ')
    print('\033[0;;m\n')  # added "\033[0;;m". without it having colored issue in colab and pycharm

def Game_State(x,y,level):
  Game_State_Sign(x,y,level)
  Game_State_Coordinate(x,y,level)

def Jump(x,y,jump):
  jump -= 1  # Keeping track of remaining jump
  if jump == -1:  # without -1, it'll count 4 times jump for 0.
      print("You're out of jump. Press 2, 4, 6 or 8 to move.")
      return x,y,0
  else:
      j = int(input())  # for jumping direction
      if j == 2:
          x += 2
      elif j == 8:
          x -= 2
      elif j == 4:
          y -= 2
      elif j == 6:
          y += 2
      return x,y,jump

def Move(x,y,jump,c):
  if c == 2:
      x += 1
  elif c == 8:
      x -= 1
  elif c == 4:
      y -= 1
  elif c == 6:
      y += 1
  elif c == 5:
      x,y,jump = Jump(x,y,jump)
  return x,y,jump

def Undo(past_x,past_y):
  return past_x,past_y

def Point(x,y,life,jump,size,total_point):
  Game_Denoter = True  # local variable
  past_value = Undo(x,y)  # storing previous value
  command=int(input())
  x,y,jump = Move(x,y,jump,command)
  list_xy = [x,y]
  # point condition
  if list_xy in Game_dict[Game_level]['Obstacle_coordinates']:
      total_point -= 5
      print("Watch Out!!! Obstacle...")
  elif list_xy in Game_dict[Game_level]['Advantage_coordinates']:
      total_point += 10
      print("Great!!! You Got an advantage...")
  # out of bound condition
  if list_xy not in full_dict:
      life -= 1
      if life == 0:
          print("Game Over!!! \nYou lost with {} points.".format(total_point))
          Game_Denoter = False
      else:
          print("Out of bound!!!\nYou lost one life. {} lives remaining.".format(life))
          x,y = past_value  # previous value. couldn't access directly in Undo() function.
  # Game state condition
  if command == 0:
      life -= 1
      if life == 0:
          print("Game Over!!! \nYou lost with {} points.".format(total_point))
          Game_Denoter = False
      else:
          print("You lost one life. {} lives remaining.".format(life))
          print("Your Current Position is:")
          Game_State(x,y,Game_level)
  # Ending point condition
  if list_xy == full_dict[-1]:
      Game_Denoter = False
      print("Game Over!!! \nYou Win with {} points.".format(total_point))
  return  x,y,Game_Denoter,life,jump,total_point


print("                  Welcome to \033[1;30;42m Memorize Your Move\033[0;;m game!!!\n")
print("  \033[2;30;47m Rules of this game: \033[0;;m\n1. You will lose one life for going out of bound.\n2. You will lose one life for checking present position state.")
print("3. Advantages will increase your point and Obstacls will decrease your point.")
print("  \033[2;30;47m How to play: \033[0;;m\nPress 8 to move up, Press 2 to move down, Press 4 to move left, Press 6 to move right.\nPress 5 for jump then press 8, 2, 4 or 6 to jump desired direction.\nPress 0 for showing present game state.\n")
print("Choose your level:\n     Press 1 for Easy\n     Press 2 for Medium\n     Press 3 for Hard\n")
Game_level=input()
if int(Game_level) == 1:
    Game_level = 'Easy'
    print("In this level, you will get {} lives, {} jumps, {} obstacles, {} advantages.\n".format(Game_dict[Game_level]['Life'],Game_dict[Game_level]['Jump'],Game_dict[Game_level]['Obstacle'],Game_dict[Game_level]['Advantage']))
elif int(Game_level) == 2:
    Game_level = 'Medium'
    print("In this level, you will get {} lives, {} jumps, {} obstacles, {} advantages.\n".format(Game_dict[Game_level]['Life'],Game_dict[Game_level]['Jump'],Game_dict[Game_level]['Obstacle'],Game_dict[Game_level]['Advantage']))
elif int(Game_level) == 3:
    Game_level = 'Hard'
    print("In this level, you will get {} lives, {} jumps, {} obstacles, {} advantages.\n".format(Game_dict[Game_level]['Life'],Game_dict[Game_level]['Jump'],Game_dict[Game_level]['Obstacle'],Game_dict[Game_level]['Advantage']))
print("     Memorize your present coordinate and obstacles, advantages to finish the game.    \n")
Game_State(0,0,Game_level)
print("Start making moves...\n")
life = Game_dict[Game_level]['Life']
jump = Game_dict[Game_level]['Jump']
size = Game_dict[Game_level]['Size']
full_dict = []
for i in range(0,size):
    for j in range(0,size):
        full_dict.append([i,j])
total_point = 0
x = 0
y = 0
Game_Denoter=True #only change to false when life will be zero or you reached the end
while(Game_Denoter):
    x,y,Game_Denoter,life,jump,total_point= Point(x,y,life,jump,size,total_point)
