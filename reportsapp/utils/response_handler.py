import json
from flask import Response


class CreateResponse(Response):
    default_status_code = 201

    def __init__(self, response, status_code=None):
        status_code = status_code if status_code else self.default_status_code
        super(CreateResponse, self).__init__(json.dumps(response), status=status_code, mimetype='application/json')


class Response404(Response):
    default_status_code = 404

    def __init__(self, response, status_code=None):
        status_code = status_code if status_code else self.default_status_code
        details_msg = '{} Does Not Exist'.format(response)
        super(Response404, self).__init__(json.dumps({'detail': details_msg}),
                                          status=status_code, mimetype='application/json')
