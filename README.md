                                          Memorize Your Move Game

             Project Idea:

             This is a console game where you (player) will need to start from your starting coordinate and need
             to reach your ending coordinate. On your way to the ending coordinate you will find obstacles and
             advantages.

             Features -

             The game has three levels - Easy, Medium and Hard. Obstacles will reduce your point and Advantages
             will increase your point. You can jump over the obstacles also. But only for fixed times. In this
             three leveled game, you will have fixed lives and jumps for each level. You can see your present
             position anytime, but for each present position state showing you will lose one of your life or if
             you go out of the bound you will lose one of your life. So, you need to memorize your last position
             and walk or jump according to that.

             Codes -

             ## Game level will be set according to user input and then all the necessary data will be fetched
             from Game_dict dictionary like number of life, advantage, obstacle, jump and size.

             ## According to the level, Initial game state will be shown with signs
               - '*' as Obstacles
               - '+' as Advantages
               - '-' as a blank path
               - 's' as starting point or current position
               - 'e' as ending point
                Another state will also appear with colored coordinates
               - Red colored coordinate numbers mean obstacles
               - Green colored coordinate numbers mean advantages
               - Black colored coordinate numbers mean blank path
               - Blue colored coordinate number means starting point or current coordinate
               - Magenta coordinate number means ending point
              These state is shown with the function Game_State() where 0,0 will be sent as parameters for
              starting point and also Game level will also be sent. Game_State() function will then call
              Game_State_Sign() and Game_State_Coordinate() functions where the code is about signs
              coordinate and colored coordinate respectively.

              ## We set total_point, x, y, Game_Denoter before entering loop with certain value.

              ## We then, in the loop, fetch x,y,Game_Denoter,life,jump,total_point with each move from Point()
              function sending those initial values as parameters.
              The loop exits when Game_Denoter is false.

              ## Point() function:
              We set Game_Denoter to True again as local variable((I don't know yet how to work with variable in
              function that declared before a function))

              ## We then store our initial point to Undo() function to use when we need to undo our move if player
              go out of bound. And then take input from player.
               - '2' for moving down
               - '8' for moving up
               - '4' for moving left
               - '8' for moving right
               - '5x' for jump; 'x' means 2/4/6/8
               - '0' for game state

              ## We then send these to calculate player next position with Move() function and update player position.

              ## We check player position if player get any advantage or obstacle and update total_point.

              ## To be out of bounds or for showing current game state, we decrease one life and if life becomes zero,
              then we return Game_Denoter False, means game over with total point. Else we retrieve previous position
              from Undo() function or show the game state.

              ## If the player position matches ending point, then we end the game with showing total point.

              ## Move() function:
               Depending on the input, we move the player avatar to up/down/right/left. If player jumps, then we call
               Jump() functions to calculate position for jumping. We then return updated x,y,and number of jumps remaining
               to the point() function.

              ## Jump() function:
               Decrease value of jump for each jump. If jump==0, then it doesn't change value of x,y but send only previous
               value. Otherwise, it then take input to which direction to jump and calculates position and return updated value.


              #### Updated: Random Dictionary

              ## Generating Random obstacle and advantage list for game dictionary.
                 # Randomly generated obstacle and advantage list via random_generator() function where the size of the
                 dictionary and the number of advantage and obstacle are passed to the function before the while loop.
                 #Used two loops for advantage and obstacle list. In each loop, two number are randomly generated in each time.
                 If the value is starting or ending point or repeated value, then we ignore it(Also in 2nd loop, we added condition
                   to ignore the values from 1st list). Else we add that value in the list. After generating specified number of
                   advantage and obstacle, we stop the loop and return these two list to add them in the Game_dict dictionary.
