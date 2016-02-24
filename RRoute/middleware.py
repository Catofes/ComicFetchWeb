import json
from RUtils.error import RError
import falcon
import time
from datetime import datetime


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = time.mktime(obj.timetuple())
        return serial
    raise TypeError("Type not serializable")


class RequireJSON(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise RError(5)

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise RError(5)


class BeginSQL(object):
    def process_request(self, req, resp):
        pass

    def process_response(self, req, resp, resource):
        if resp.status != falcon.HTTP_200:
            if 'request' in req.context.keys():
                request = req.context['request']
            else:
                request = None


class JSONTranslator(object):
    def process_request(self, req, resp):
        # req.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333
        if req.content_length in (None, 0):
            # Nothing to do
            return

        body = req.stream.read()
        if not body:
            raise RError(6)

        try:
            req.context['request'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise RError(7)

    def process_response(self, req, resp, resource):
        if 'result' not in req.context.keys():
            return

        resp.body = json.dumps(req.context['result'], default=json_serial)
