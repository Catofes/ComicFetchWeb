__author__ = 'herbertqiao'
import falcon
from falcon import HTTPError

Error_text = {
    0: ['Unknown Error.',
        falcon.HTTP_500],
    1: ['SQL Error.',
        falcon.HTTP_500],
    2: ['Token Required.',
        falcon.HTTP_400],
    3: ['Login Required',
        falcon.HTTP_403],
    4: ['Login Failed',
        falcon.HTTP_403],
    5: ['Only Json Is Accepted or Sent',
        falcon.HTTP_400],
    6: ['Empty Request Body',
        falcon.HTTP_400],
    7: ['Malformed JSON',
        falcon.HTTP_400],
    8: ['Password Required',
        falcon.HTTP_403],
    9: ['Password Error',
        falcon.HTTP_403],
    10: ['Illegal URL',
         falcon.HTTP_403],
    11: ['Duplicate URL',
         falcon.HTTP_403],
    12: ['Unknown ID',
         falcon.HTTP_403],
    13: ['Missing Parameters',
         falcon.HTTP_403],
    403: ['',
          falcon.HTTP_403],
    404: ['',
          falcon.HTTP_404]
}


class RError(HTTPError):
    def __init__(self, code=0):
        global Error_text
        self.code = code
        if self.code not in Error_text.keys():
            self.code = 0
        self.text = Error_text[self.code][0]
        self.http_code = Error_text[self.code][1]
        HTTPError.__init__(self, self.http_code, self.text, code=self.code)
