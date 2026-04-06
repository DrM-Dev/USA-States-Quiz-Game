#USA States Quiz Game  by    Dr.M-Dev
#========================imports

import pandas
import pandas as pd
from turtle import Turtle,Screen
from pandas.io.sas.sas_constants import encoding_length
#this is actually important (if using pycharm) don't delete :)



print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

print("******** WELCOME TO USA States Quiz Game  -   By: Dr.m DEV *********")

#==========================================================================================================
#==========================================================================================================
#==========================================================================================================
#==========================================================================================================
##################

#Setup
screen = Screen()
screen.setup(1000,600)
screen.bgpic("bg_art.png")
screen.title("USA States Quiz Game")
#
screen.addshape("blank_states_img.gif")
#----------------------------------------
pen = Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")
#
state_map = Turtle()
state_map.shape("blank_states_img.gif")
#----------------------------------------
player_correct_points = 0
player_false_points = 0
#
states_list = []
states_guessed = []


##===========================================================================Quiz System
states_dataframe = pd.read_csv("50_states.csv")
#
states_column = states_dataframe.state
states_list = list(states_column)
states_list_fix_name = []
#teak-names: Texas -> texas (to avoid errors)
for states in states_list:
    fixed_name = states.lower()
    states_list_fix_name.append(fixed_name)
#------------------------
states_list.clear()
states_list = states_list_fix_name.copy()
# #debug
# print(states_list)

#===========================================================================Quiz Input:
def start_test():
    #global-constants
    global states_dataframe
    global states_column
    #global-vars
    global player_correct_points
    global player_false_points
    global states_list
    global states_guessed

    #################quiz-switch
    test_is_on = True
    #----

    while test_is_on:
        new_state_guess = screen.textinput(title="Enter a state 🇺🇸",prompt="guess a state name here :)\n\n<!>\nif you want to stop guessing an get your score\ntype \"END\" and press [OK]").lower()
        ##---------##
        if new_state_guess == "end":
            print("WRONG!")
            final_score = player_correct_points - player_false_points
            #
            screen.textinput(title="Quiz Over",
                             prompt=f"Your final score is: {final_score}\nwe calculated your right guesses minus every incorrect guess")

            #----------------------------------------------------
            #the states you got right and the ones you got wrong:
            all_states = []
            guessed_or_missed = []
            #--------
            null = "Missed🚫"
            right = "Guessed✅"
            ####
            global states_guessed
            states_guessed_fix = []
            # |
            # v
            for guess in states_guessed:
                guess = guess.lower()
                states_guessed_fix.append(guess)
            #--
            states_guessed.clear()
            states_guessed.extend(states_guessed_fix)

            #######################
            for state in states_list:
                all_states.append(state)
                #-----
                if state in states_guessed: #---->LOWER EVERY NAME IN STATES GUESSED!
                    print(f">>>>>>>>>>>You guessed the following state:{state}")
                    guessed_or_missed.append(right)
                #--------
                else:
                    guessed_or_missed.append(null)

            #---------------#
            state_test_result = {
                "All States": [
                    "-",
                ],
                "Guessed / Missed" : [
                    "-",
                ]
            }

            # ---------------#
            # notification
            print(f"The test is calculating the states you missed and guessed,\nand saving it in a csv-file:\n\n\"States you guessed and missed.csv\"\n\ngo ahead and check it :)")
            screen.textinput(title="PRINTING RESULTS",
                             prompt=f"The test is calculating the states you missed and guessed,\nand saving it in a csv-file:\n\n\"States you guessed and missed.csv\"\n\ngo ahead and check it :)")

            # ---------------#
            # for state_m in all_states:
            #     state_test_result["States you missed"].append(state_m)
            # ####
            # for state_g in guessed_or_missed:
            #     state_test_result["States you guessed"].append(state_g)
            #XXXXXX
            state_test_result["All States"].extend(all_states)
            state_test_result["Guessed / Missed"].extend(guessed_or_missed)



            #debug
            # print(states_guessed)
            # #
            # print("\n")
            # print(len(state_test_result["Guessed / Missed"]))
            # print(guessed_or_missed)
            # print("\n")
            # print(len(state_test_result["All States"]))
            # print(all_states)

            #---------------##---------------##---------------##---------------#
            test_result_df = pandas.DataFrame(state_test_result)
            test_result_df.to_csv("States you guessed and missed.csv")
            break


        #--=----=----=----=----=----=----=--
        if new_state_guess in states_guessed:
            #debug
            # print("name already guessed :)")
            #
            screen.textinput(title="Already Guessed it :)",
                             prompt="press [OK] to guess again")
            #
        else:
            ##---------##
            if new_state_guess in states_list:
                #debug
                print("CORRECT!")
                #
                try:
                    ##########################################################
                    # fixing input to fit the CSV-Dataframe
                    new_state_guess = new_state_guess.title()#DON'T USE .capitalize() since it won't work with NewYokr or similar names xD

                    # __________________________________________visualization
                    state_row_detector = states_dataframe[states_column == str(new_state_guess)]   # now we got the row that the player guessed
                    # DEBUG
                    # to get the integer value YOU MUST! use .item to avoid getting other data-types involved!
                    # print(f"name guessed {new_state_guess}")
                    # print(f"THIS {state_row_detector}")  # checking data-series / row
                    #
                    x = (state_row_detector["x"].item())
                    y = (state_row_detector["y"].item())
                    # DEBUG
                    # print(f"xcor = {x}, ycor = {y}")  # getting x cor
                    ##################################
                    pen.penup()
                    pen.goto(int(x),int(y))
                    pen.write(f"{new_state_guess}", align="Center", font=("Arial",7,"bold"))
                    #____________
                    #Clip it & Ship it (I mean append it) \\
                    states_guessed.append(new_state_guess)
                    player_correct_points += 1

                except ValueError:
                    # print("""Spelling Error CLOSE! the spelling of that state was incorrect\n->try again like \"New York\"\n\n[no points will be taken] :)")
                    #
                    screen.textinput(title="Spelling Error",
                                     prompt="CLOSE! the spelling of that state was incorrect\n->try again like \"New York\"\n\n[no points will be taken] :)\n,press [OK] to guess again")
                    #
                # ____________________________________
            else:
                # debug
                print("WRONG!")
                #
                screen.textinput(title="WRONG GUESS!",
                                 prompt="press [OK] to guess again")
                #
                #-----
                player_false_points += 1

        #+++++++++++++++++++++++++++++++++++++++++++++END-GAME:
        if len(states_guessed) >= 50:
            print("HOLY MOLY YOU WON! you have guessed all 50 states! like a red-blooded American B^]")
            #
            #
            screen.textinput(title="HOLY MOLY YOU WON!",
                             prompt="you have guessed all 50 states! like a red-blooded American B^]")
            #
            #-----
            test_is_on = False



#===========================================================================App Launch:
start_test()


#_________________________________________________________________
screen.mainloop()
