"""
Manage CustomResponse and handle different status code, more handy and more control.
status : 201, 204, 404, 400

Extend Response Module and CustomResponse method.
"""

import json
from flask import Response

__all__ = ['CreateResponse', 'Response404', 'BadResponseAlreadyExist', 'DeleteResponse', 'MethodNotImplemented']


class CreateResponse(Response):
    """ CreateResponse for CREATE method and returns 201-CREATED """
    default_status_code = 201

    def __init__(self, response, status_code=None):
        status_code = status_code if status_code else self.default_status_code
        super(CreateResponse, self).__init__(json.dumps(response), status=status_code, mimetype='application/json')


class Response404(Response):
    """ Response404 for OBJECT-NOT-FOUND and returns 404-NOT-FOUND """
    default_status_code = 404

    def __init__(self, response, status_code=None):
        status_code = status_code if status_code else self.default_status_code
        detail_msg = '{} Does Not Exist'.format(response)
        super(Response404, self).__init__(json.dumps({'detail': detail_msg}),
                                          status=status_code, mimetype='application/json')


class BadResponseAlreadyExist(Response):
    """ BadResponseAlreadyExist for ALREADY-EXIST-OBJECT and returns 400-BAD-REQUEST """
    default_status_code = 400

    def __init__(self, response, status_code=None):
        status_code = status_code if status_code else self.default_status_code
        detail_msg = response
        super(BadResponseAlreadyExist, self).__init__(json.dumps({'detail': detail_msg}),
                                                      status=status_code, mimetype='application/json')


class DeleteResponse(Response):
    """ DeleteResponse for DELETE method and returns 201-NOT-FOUND """
    default_status_code = 204

    def __init__(self, response, status_code=None):
        status_code = status_code if status_code else self.default_status_code
        detail_msg = response
        super(DeleteResponse, self).__init__(json.dumps({'detail': detail_msg}),
                                             status=status_code, mimetype='application/json')


class MethodNotImplemented(Response):
    """ DeleteResponse for DELETE method and returns 201-NOT-FOUND """
    default_status_code = 405

    def __init__(self, response, status_code=None):
        status_code = status_code if status_code else self.default_status_code
        detail_msg = 'Method Not Implemented'
        super(MethodNotImplemented, self).__init__(json.dumps({'detail': detail_msg}),
                                             status=status_code, mimetype='application/json')
