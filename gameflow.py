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

    def __repr__(self):
        return "{} occupying the post number {:d}".format(self.name, self.post)


def load_question():
    filename = input("Give the name of the .odt file without extension")
    path = "questions/" + filename
    questions = [["Stolica Paragwaju ?", "Asuncion"], ["Stolica Boliwii ?", "La Paz"],
                 ["Stolica Chile ?", "Santiago"]]
    return questions


# getting the info about players
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
    return players


def stage1(players):
    questions = load_question()
    num_of_players = len(players)
    for n in range(num_of_players * 3):
        post_num = (n % (num_of_players + 1)) + 1
        current_player = next((x for x in players if x.post == post_num), None)
        if not current_player:
            continue
        print("Now responding: {}, player number {:d}, chances left: {:d}".format(current_player.name,
                                                                                  current_player.post,
                                                                                  current_player.chances))
        try:
            print("Question for :{}".format(questions[n][0]))
            print("Correct answer: {}".format(questions[n][1]))
        except IndexError:
            print("The pool of questions has ended")

        correct = input("Correct?")

        if not correct:
            current_player.chances -= 1
        if current_player.chances == 0:
            players.remove(current_player)
    print("The players going to the next stage are:")
    pprint(players)
    return players


def main():
    players = get_players()
    print("We have {:d} players taking part in our game:".format(len(players)))
    pprint(players)
    print("Let's begin!")

    # STAGE1
    players_after_1stage = stage1(players)
    print(players_after_1stage)

    # # STAGE2
    # players_after_2stage = stage1(players)
    # # STAGE3
    # winner = stage1(players)
    #
    # print(winner)


if __name__ == '__main__':
    main()
