from DatabaseManager import DatabaseManager
from Logger import logger


class DatabaseHelper(DatabaseManager):
    def __init__(self, connect_str):
        super(DatabaseHelper, self).__init__(connect_str)

    def get_replies_question_forum(self):
        replies_question_forum_db = self.my_query("""select *
        from replies
        join questions on questions.questions_id = replies.questions_id
        join forum_details on questions.forum_details_id = forum_details.forum_details_id
        """, None, 'dict')
        replies_question_forum = {}
        for reply_question_forum in replies_question_forum_db:
            forum_id = reply_question_forum[10]
            if forum_id not in replies_question_forum.keys():
                replies_question_forum[forum_id] = {}
            question_id = reply_question_forum[4]
            if question_id not in replies_question_forum[forum_id].keys():
                replies_question_forum[forum_id][question_id] = {}
                replies_question_forum[forum_id][question_id]['replies_text'] = []
            replies_question_forum[forum_id][question_id]['replies_text'].append(reply_question_forum[1])
        return replies_question_forum

    def get_forums(self):
        forums = {}
        for forum in self.my_query('select * from forum_details', None, 'dict'):
            forums[forum['forum_details_id']] = {}
            forums[forum['forum_details_id']]['name'] = forum['name']
            forums[forum['forum_details_id']]['url'] = forum['url']

        return forums

    def get_forums_names(self):
        forums_names = []

        for forum in self.my_query('select name from forum_details', None, 'dict'):
            forums_names.append(forum['name'])

        return forums_names

    def get_questions(self):
        return self.my_query("select * from questions", None, 'dict')

    def get_questions_content(self):
        data = []
        questions_db = self.my_query("select * from questions", None, 'dict')

        for question in questions_db:
            content = question[5]
            if content is not None:
                data.append(content)
        return data

    def get_questions_by_forum(self):
        data = []
        target = []
        target_names = []

        questions_forum_db = self.my_query(
            "select * from questions join forum_details on forum_details.forum_details_id = questions.forum_details_id",
            None,
            'dict')

        for question_forum in questions_forum_db:
            content = question_forum['content']
            if question_forum['name'] not in target_names:
                target_names.append(question_forum['name'])
            if content is not None:
                data.append(content)
                target.append(target_names.index(question_forum['name']))

        return data, target, target_names
