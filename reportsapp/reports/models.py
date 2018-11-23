from config import mongo_db


class UserDocument():
    """
    Since we are using pymongo, we don't have ORM like MongoEngine.
    We can use this small python-class for document validation and save.
    """

    def __init__(self):
        pass

    def validate_user_data(self, document):
        """ Validate Document's format """
        pass

    def get_or_create(self, document):
        """ Create Reports Document """
        report_doc = mongo_db.db.users.insert_one(document)
        return report_doc.inserted_id

    def delete_user(self, document):
        """ Delete Reports Document """

    def fetch_user(self, username=None, *args, **kwargs):
        """ Find/FindAll Reports Document """
        if username:
            query = {'name': username}
            return mongo_db.db.users.find(query, {'_id': 0})
        return mongo_db.db.users.find()


users_doc = UserDocument()


class ReportsDocument():
    """
    Since we are using pymongo, we don't have ORM like MongoEngine.
    We can use this small python-class for document validation and save.
    """

    def __init__(self):
        pass

    def validate_reports_document(self, document):
        """ Validate Document's format """
        pass

    def create_reports_document(self, document):
        """ Create Reports Document """
        report_doc = mongo_db.db.users.insert_one(document)
        return report_doc.inserted_id

    def delete_reports_document(self, document):
        """ Delete Reports Document """

    def fetch_reports_document(self, username=None, *args, **kwargs):
        """ Find/FindAll Reports Document """
        if username:
            query = {'name': username}
            return mongo_db.db.users.find(query, {'_id': 0})
        return mongo_db.db.users.find()


reports_doc = ReportsDocument()
