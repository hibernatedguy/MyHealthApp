from config import monod_db, app_info


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
        pass

    def delete_reports_document(self, document):
        """ Delete Reports Document """

    def fetch_reports_document(self, username, *args, **kwargs):
        """ Find/FindAll Reports Document """
        pass
