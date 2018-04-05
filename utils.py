import os
import simpledb_connection

from playsound import playsound

path_for_sounds = os.getcwd()


def tag_question_done(question_id):
    conn = simpledb_connection.DbConnection('questions.db')
    sql = "UPDATE questions SET done=1 WHERE id={}".format(question_id)
    conn.c.execute(sql)
    conn.commit()


def load_questions(num, stage):
    conn = simpledb_connection.DbConnection('questions.db')
    sql = "SELECT id,question,answer FROM questions WHERE stage={} AND done=0 ORDER BY id LIMIT {}".format(stage,
                                                                                                           1 + num * 2)
    conn.c.execute(sql)
    questions = conn.c.fetchall()
    ids = [x[0] for x in questions]
    ids = str(ids).replace(']', ')').replace('[', '(')
    sql = "UPDATE questions SET done=1 WHERE id in {}".format(ids)
    conn.c.execute(sql)
    conn.commit()
    return questions


def restore_all_questions():
    conn = simpledb_connection.DbConnection('questions.db')
    sql = "UPDATE questions SET done=0"
    conn.c.execute(sql)
    conn.commit()


def play_intro_song():
    path = path_for_sounds + "\\sounds\\themesong.mp3"
    playsound(path, True)


def play_correct_sound():
    path = path_for_sounds + "\\sounds\\correct.mp3"
    playsound(path, True)


def play_incorrect_sound():
    path = path_for_sounds + "\\sounds\\incorrect.mp3"
    playsound(path, True)


def play_outofgame_sound():
    path = path_for_sounds + "\\sounds\\out_of_game.mp3"
    playsound(path, True)
