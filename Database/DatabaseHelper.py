from Database.DatabaseManager import DatabaseManager


class DatabaseHelper(DatabaseManager):
    """
    Class that inherits from DatabaseManager to extend it with data preprocessing functions used several times in other
    files.
    """
    def __init__(self, connect_str):
        """
        A DatabaseHelper instance must be initialized with a connection string containing the database name and user.
        :param connect_str: provides database connection details : db name, user, password, ...
        :type connect_str: str
        """
        super(DatabaseHelper, self).__init__(connect_str)


    def get_replies_question_forum(self):
        """
        Retrieves all replies, groups them by question, and groups the questions by forum
            :return: returns the grouped data
            :rtype: dict
        """
        replies_question_forum_db = self.my_query("""select *
        from replies
        join questions on questions.questions_id = replies.questions_id
        join forum_details on questions.forum_details_id = forum_details.forum_details_id
        """, None, fetch_to_dict=True)
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
        """
        Retrieves the forums details and returns them in a dictionary.
        :return: returns the forums details (id, name, url)
        :rtype: dict
        """
        forums = {}
        for forum in self.my_query('select * from forum_details', None, fetch_to_dict=True):
            forums[forum['forum_details_id']] = {}
            forums[forum['forum_details_id']]['name'] = forum['name']
            forums[forum['forum_details_id']]['url'] = forum['url']

        return forums

    def get_forums_names(self):
        """
        Retrieves and returns the forum names in a list.
        :return: the forum names
        :rtype: list
        """
        forums_names = []

        for forum in self.my_query('select name from forum_details', None, fetch_to_dict=True):
            forums_names.append(forum['name'])

        return forums_names

    def get_questions(self):
        """
        Retrieves and returns the questions in a dictionary.
        :return: returns the questions from the database
        :rtype: dict
        """
        return self.my_query("select * from questions", None, fetch_to_dict=True)

    def get_questions_content(self):
        """
        Retrieves only the content of the questions and returns them in an list.
        :return: returns the contents of every question.
        :rtype: list
        """
        data = []
        questions_db = self.my_query("select * from questions", None, fetch_to_dict=True)

        for question in questions_db:
            content = question[5]
            if content is not None:
                data.append(content)
        return data

    def get_questions_titles_by_forum(self):
        """
        Retrieves the questions grouped by forum and returns a tuple of lists used in some ML algorithms
        :return: returns a tuple of lists, the first one contains the contents of the questions, the second the forum index
         for each question, the third the forum names (used as classifying labels called "target")
        :rtype: tuple
        """

        data = []
        target = []
        target_names = []

        questions_forum_db = self.my_query(
            "select * from questions join forum_details on forum_details.forum_details_id = questions.forum_details_id",
            None,
            fetch_to_dict=True)

        for question_forum in questions_forum_db:
            content = question_forum['text']
            if question_forum['name'] not in target_names:
                target_names.append(question_forum['name'])
            if content is not None:
                data.append(content)
                target.append(target_names.index(question_forum['name']))

        return data, target, target_names
