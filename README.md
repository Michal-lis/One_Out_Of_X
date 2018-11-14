# One_Out_Of_X
This project is a game simulating famous Polish television quiz show named "1 z 10" (1 out of 10).
Written in Python 3, with questions found on the internet as .odt files and and parsed into SQLite DB.

Rules:
Each player has 3 chances at the beginning
This television quiz show includes 3 stages:
    1st stage - every player is asked 3 questions. In order to get to the next stage the players have to answer correctly at
 least twice. The wrong answers are subtracted from the chances of the player.
    2nd stage - the player occupying the post number 1 is asked a question, if he answers correctly than he is the one to 
select the player who will be answering the next questions. For every wrong answer the players are taken 1 chance. This 
stage ends when there are only 3 players having any chance left. The remaining 3 players take part in the last stage.
    3rd stage - First, the chances from the previous stage are converted into points in ratio 1:1 and the chances are 
    restored (each player has 3 again). The players are asked question in the form 'first come, first served '. . 
    For each correct answer the players are given 10 pts. The first one to score 30 points than may choose to answer 
    himself (the number of points gained by answering correctly is doubled) or may nominate any opponent. When the 
    opponent answers correctly - he may choose what to do next. The number of questions is limited to 40. The one who 
    has the highest number of points or the ones who is the only one with points left - wins. 
