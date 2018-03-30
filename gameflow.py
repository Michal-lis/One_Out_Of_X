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
import os

from playsound import playsound
from pprint import pprint


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


def load_questions():
    filename = input("Give the name of the .odt file without extension")
    path = "questions/" + filename
    questions = [["Stolica Paragwaju ?", "Asuncion"], ["Stolica Boliwii ?", "La Paz"],
                 ["Stolica Chile ?", "Santiago"]]
    return questions


# getting the initial info about players
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


def play_correct_sound(path):
    path = path + "\\sounds\\correct.mp3"
    playsound(path, True)


def play_incorrect_sound(path):
    path = path + "\\sounds\\incorrect.mp3"
    playsound(path, True)


def select_player(players, num_of_players=None, question_number=None, select=False):
    if select:
        while True:
            players_to_choose_from = [x.post for x in players]
            num_chosen = int(input("Which player should answer now?"))
            if num_chosen in players_to_choose_from:
                break
    else:
        num_chosen = (question_number % (num_of_players + 1)) + 1
    player = next((player for player in players if player.post == num_chosen), None)
    return player


def ask_question(current_player, question, path, out_of_range=False):
    print("Now responding: {}, player number {:d}, chances left: {:d}".format(current_player.name,
                                                                              current_player.post,
                                                                              current_player.chances))
    if not out_of_range:
        print("Question for :{}".format(question[0]))
        print("Correct answer: {}".format(question[1]))
    correct = int(input("Correct?"))
    if not correct:
        current_player.chances -= 1
        play_incorrect_sound(path)
    else:
        play_correct_sound(path)


def check_current_player_chances(players, current_player):
    if current_player.chances == 0:
        players.remove(current_player)


def check_winner(players):
    if len(players) == 1:
        winner = players[0]
        print("The winner is: {}".format(winner))


def stage1(players, path_for_sounds):
    print("Let's begin the first stage")
    questions1 = load_questions()
    num_of_players = len(players)
    for n in range(num_of_players * 3):
        current_player = select_player(players, num_of_players, n)
        if not current_player:
            continue
        try:
            question = questions1[n]
            ask_question(current_player, question, path_for_sounds)
        except IndexError:
            print("The pool of questions has ended")
            ask_question(current_player, None, path_for_sounds, out_of_range=True)
        check_current_player_chances(players, current_player)
        check_winner(players)

    print("The players going to the SECOND STAGE are:")
    for player in players:
        print(player)
    return players


def stage2(players, path_for_sounds):
    print("Lets begin the second stage!")
    current_player = players[0]
    questions2 = [["Stolica Laosu ?", "Vientian"], ["Stolica Kambodży ?", "Phnom Penh"],
                  ["Stolica Wietnamu ?", "Hanoi"]]
    # zmienic tutaj paramter na maksymalna liczbe pytan z drugiego etapu
    for n in range(5):
        try:
            question = questions2[n]
            ask_question(current_player, question, path_for_sounds)
        except IndexError:
            print("The pool of questions has ended")
            ask_question(current_player, None, path_for_sounds, out_of_range=True)
        check_current_player_chances(players, current_player)
        check_winner(players)
        current_player = select_player(players, select=True)
    print("The players going to the FINAL STAGE are:")
    for player in players:
        print(player)
    return players


def main():
    players = get_players()
    path_for_sounds = os.getcwd()

    ######################### STAGE1
    players_after_1stage = stage1(players, path_for_sounds)

    ######################### STAGE2
    players_after_2stage = stage2(players, path_for_sounds)
    print(players_after_1stage)

    # # STAGE3
    # winner = stage1(players)
    #
    # print(winner)


if __name__ == '__main__':
    main()
