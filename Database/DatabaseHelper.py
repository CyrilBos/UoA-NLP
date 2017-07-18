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


    def get_community_id(self, community_name):
        return self.select_query('select community_id from community where community_name = %s', (community_name,))[0]

    def get_replies_question_forum(self, community_name='Business'):
        """
        Retrieves all replies, groups them by question, and groups the questions by forum
            :return: returns the grouped data
            :rtype: dict
        """
        replies_question_forum_db = self.select_query("""select *
        from replies
        join question on question.question_id = replies.question_id
        join forum_details on question.forum_details_id = forum_details.forum_details_id
        where community_id = %s
        """, self.get_community_id(community_name), fetch_to_dict=True)
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

    def get_forums(self, community_name='Business'):
        """
        Retrieves the forums details and returns them in a dictionary.
        :return: returns the forums details (id, name, url)
        :rtype: dict
        """
        forums = {}
        for forum in self.select_query('select * from forum_details where community_id = %s', self.get_community_id(community_name), fetch_to_dict=True):
            forums[forum['forum_details_id']] = {}
            forums[forum['forum_details_id']]['name'] = forum['name']
            forums[forum['forum_details_id']]['url'] = forum['url']

        return forums

    def get_forums_names(self, community_name='Business'):
        """
        Retrieves and returns the forum names in a list.
        :return: the forum names
        :rtype: list
        """
        forums = self.get_forums_names()
        forums_names = []
        for forum in forums:
            forums_names.append(forums[forum]['name'])

        return forums_names

    def get_questions(self, community_name='Business'):
        """
        Retrieves and returns the questions in a dictionary.
        :return: returns the questions from the database
        :rtype: dict
        """
        return self.select_query("""select * from question join forum_details on
                                    forum_details.forum_details_id = question.forum_details_id
                                 where community_id = %s""", self.get_community_id(community_name), fetch_to_dict=True)

    def get_questions_content(self, community_name='Business'):
        """
        Retrieves only the content of the questions and returns them in an list.
        :return: returns the contents of every question.
        :rtype: list
        """
        contents = []
        questions_db = self.get_questions(community_name)

        for question in questions_db:
            content = question['content']
            if content is not None:
                contents.append(content)
        return contents

    def get_questions_titles_by_forum(self, community_name='Business'):
        """
        Retrieves the questions grouped by forum and returns a tuple of lists used in some ML algorithms
        :return: returns a tuple of lists, the first one contains the contents of the questions, the second the forum index
         for each question, the third the forum names (used as classifying labels called "target")
        :rtype: tuple
        """

        data = []
        target = []
        target_names = []

        questions_forum_db = self.select_query(
            "select * from question join forum_details on forum_details.forum_details_id = question.forum_details_id"
            "where community_id = %s",
            self.get_community_id(community_name),
            fetch_to_dict=True)

        for question_forum in questions_forum_db:
            content = question_forum['text']
            if question_forum['name'] not in target_names:
                target_names.append(question_forum['name'])
            if content is not None:
                data.append(content)
                target.append(target_names.index(question_forum['name']))

        return data, target, target_names

    def get_training_data(self, community_name='Business'):
        training_data = self.select_query("""select training_data.content, category_name from training_data join training_data_category on training_data.training_data_category_id = training_data_category.training_data_category_id
                        join question on question.question_id = training_data.question_id
                        join forum_details on forum_details.forum_details_id = question.forum_details_id
                        where community_id = %s""", self.get_community_id(community_name), fetch_to_dict=True)
        data = []
        target = []
        target_names = [row[0] for row in self.select_query('select category_name from training_data_category order by 1 asc', fetch_to_dict=False)]

        for row in training_data:
            data.append(row['content'])
            target.append(target_names.index(row['category_name']))

        return data, target, target_names