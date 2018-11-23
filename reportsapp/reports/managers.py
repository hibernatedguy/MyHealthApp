import json
from config import mongo_db
from bson.json_util import dumps

__all__ = ['users_document', 'reports_document']


class UserDocumentManager():
    """
    MongoDB manager to handle user and reports
    user_collections = [{'username': <username-goes-here>}]
    """

    def __init__(self):
        pass

    def get_or_create(self, document):
        """
        Check if user is already exists or not?
        If user already exist then do nothing else create user.
        """
        user_exists = json.loads(dumps(self.fetch_users(username=document.get('username'))))
        if not user_exists:
            user_doc = mongo_db.db.users.insert_one(document)
            return user_doc.inserted_id, True
        return '', False

    def delete_users(self, username):
        """ Delete Reports Document """
        query = {'username': username}
        delete_user = mongo_db.db.users.delete_many(query)
        delete_related_reports = mongo_db.db.reports.delete_many(query)

        # send deleted counts
        deleted_user_count = delete_user.deleted_count
        deleted_report_count = delete_related_reports.deleted_count
        return deleted_user_count, deleted_report_count

    def fetch_users(self, username=None, *args, **kwargs):
        """ Find/FindAll User """
        if username:
            query = {'username': username}
            return mongo_db.db.users.find(query)
        return mongo_db.db.users.find()


users_document = UserDocumentManager()


class ReportsDocumentManager():
    """
    MongoDB manager to handle user and reports
    reports_collections = [{'username': <username-goes-here>}]
    """

    def __init__(self):
        pass

    def validate_reports_data(self, document):
        """ Validate Document's format """
        pass

    def create_reports(self, document):
        """ Create Reports and send user information to user-doc-manager to create the same. """
        report_doc = mongo_db.db.reports.insert_one(document)
        user, status = users_document.get_or_create({'username': document.get('username')})
        print(user, status)
        return report_doc.inserted_id

    def delete_reports(self, username):
        """ Delete Reports for a user"""
        query = {'username': username}
        delete_related_reports = mongo_db.db.reports.delete_many(query)
        return {'details': '#{}:reports document deleted.'.format(delete_related_reports.deleted_count)}

    def fetch_reports(self, username=None, *args, **kwargs):
        """ Find/FindAll Reports """
        if username:
            query = {'username': username}
            return mongo_db.db.reports.find(query)
        return mongo_db.db.reports.find()


reports_document = ReportsDocumentManager()
