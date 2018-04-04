import sqlite3


class DbConnection:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, timeout=10)
        self.c = self.conn.cursor()

    def __enter__(self):
        return self

    def execute(self, query):
        self.c.execute(query)
        return self.c

    def commit(self):
        self.conn.commit()

    def close(self):
        self.c.close()
        self.conn.close()

    def insert_questions(self, questions):
        self.execute(
            "CREATE TABLE IF NOT EXISTS questions(id INTEGER, question TEXT, answer TEXT, question_number INTEGER,stage INTEGER,done NUMERIC, episode_number INTEGER, series_number INTEGER, PRIMARY KEY(id))")

        for quest_dict in questions:
            columns = ', '.join(quest_dict.keys())
            placeholders = ', '.join('?' * len(quest_dict))
            sql = 'INSERT INTO questions ({}) VALUES ({})'.format(columns, placeholders)
            self.c.execute(sql, list(quest_dict.values()))

    def get_questions_for_episode(self, series, episode):
        # returns list of questions as list in order:
        # id, question, answer, question number, stage, done, epi_num, series_num
        sql = 'SELECT * FROM questions WHERE episode_number={} AND series_number={}'.format(episode, series)
        self.c.execute(sql)
        questions = self.c.fetchall()
        return questions
