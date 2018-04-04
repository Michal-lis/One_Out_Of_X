"""Rules:
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
    has the highest number of points or the ones who is the only one with points left - wins. """
from pprint import pprint
from utils import play_incorrect_sound, play_correct_sound, play_intro_song, load_questions


class Question():
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

    def __repr__(self):
        return self.question_text


class Player():
    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.score = 0
        self.chances = 3
        self.asked = 0

    def __repr__(self):
        return "{} occupying the post number {:d} with {:d} chances left".format(self.name, self.post, self.chances)


def get_players():
    players = []
    while True:
        try:
            num_of_players = int(input("How many players are going to play this game?"))
        except ValueError:
            print("Please enter a number.")
            continue
        else:
            break

    for n in range(num_of_players):
        post = n + 1
        name = input("Name of player %d:" % post)
        player = Player(name, post)
        players.append(player)
    print("We have {:d} players taking part in our game:".format(len(players)))
    pprint(players)
    return players


def select_player(players, num_of_players=None, question_number=None, select=False):
    if select:
        while True:
            players_to_choose_from = [x.post for x in players]
            pprint(players_to_choose_from)
            num_chosen = int(input("Which player should answer now?"))
            if num_chosen in players_to_choose_from:
                break
    else:
        num_chosen = (question_number % (num_of_players + 1)) + 1
    player = next((player for player in players if player.post == num_chosen), None)
    return player


def ask_question(current_player=None, question=None):
    if current_player:
        print("Now responding: {}, player number {:d}, chances left: {:d}".format(current_player.name,
                                                                                  current_player.post,
                                                                                  current_player.chances))
    if question:
        print("Question nr {}: {}".format(question[0], question[1]))
        print("Correct answer: {}".format(question[2]))
    correct = int(input("Correct?"))
    return correct


def check_current_player_chances(players, current_player, correct, stage=None):
    if not correct:
        current_player.chances -= 1
        play_incorrect_sound()
    else:
        play_correct_sound()
    if stage == "stage1":
        chances_to_die = 1
    if stage in ["stage2", "final_stage"]:
        chances_to_die = 0
    if current_player.chances == chances_to_die:
        players.remove(current_player)
        print("Player {} is out of the game!".format(current_player.name))


def check_winner(players, end=False):
    if end:
        winner
    if len(players) == 1:
        winner = players[0]
        print("The winner is: {}".format(winner))
        return winner


        #########################        STAGE1        #########################


def stage1(players):
    print("Let's begin the first stage")
    questions1 = load_questions(len(players), stage=1)
    num_of_players = len(players)
    for n in range((num_of_players + 1) * 2):
        current_player = select_player(players, num_of_players, n)
        if not current_player:
            continue
        try:
            question = questions1[n]
            correct = ask_question(current_player, question)
        except IndexError:
            print("The pool of questions has ended")
            correct = ask_question(current_player)
        check_current_player_chances(players, current_player, correct, stage="stage1")
        check_winner(players)

    print("The players going to the SECOND STAGE are:")
    for player in players:
        print(player)
    return players


    #########################        STAGE2        #########################


def stage2(players):
    print("Lets begin the second stage!")
    first_question = True
    current_player = players[0]
    questions2 = load_questions(25, stage=2)
    question_counter = 0
    while len(players) > 3:
        if not first_question:
            current_player = select_player(players, select=True)
        else:
            first_question = False
        try:
            question = questions2[question_counter]
            correct = ask_question(current_player, question)
        except IndexError:
            print("The pool of questions has ended")
            correct = ask_question(current_player)
        check_current_player_chances(players, current_player, correct, stage="stage2")
        question_counter += 1
    print("The players going to the FINAL STAGE are:")
    for player in players:
        print(player)
    return players


    #########################        FINAL STAGE        #########################

# ogarnij flow 3 stage + napisz return questions
def final_stage(players):
    print("Lets begin the final stage!")
    first_30_points = False
    max_num_of_questions = 40
    questions3 = load_questions(max_num_of_questions, stage=3)
    if not first_30_points:
        for n in range(max_num_of_questions):
            question_counter = n
            try:
                question = questions3[question_counter]
                correct = ask_question(question=question)
            except IndexError:
                print("The questions ended - this is the end of the game.")
                check_winner(players, end=True)
                break
            current_player = select_player(players, select=True)
            check_current_player_chances(players, current_player, correct, stage="final_stage")
            print("Player scores: {}, {}, {}".format(players[0].score, players[1].score, players[2].score))
            if check_winner(players):
                break


def main():
    play_intro_song()
    players = get_players()
    # players = stage1(players)
    # players = stage2(players)
    final_stage(players)


if __name__ == '__main__':
    main()
