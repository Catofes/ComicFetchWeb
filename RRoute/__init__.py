# -*- coding: UTF-8 -*-
from wsgiref import simple_server
import falcon
import RRoute.middleware
import RUtils
import traceback
import RComic.comic
from pymongo import MongoClient


class Route:
    @staticmethod
    def error_handle(ex, req, resp, params):
        if isinstance(ex, falcon.HTTPError):
            raise ex
        else:
            traceback.print_exc()
            raise RUtils.RError(0)

    def __init__(self):
        self.db = MongoClient()
        self.app = falcon.API(middleware=[
            middleware.RequireJSON(),
            middleware.JSONTranslator(),
            middleware.BeginSQL()
        ]
        )
        self.app.add_error_handler(Exception, handler=Route.error_handle)

        comic_list = RComic.comic.ComicList(self.db)
        comic = RComic.comic.Comic(self.db)
        watch = RComic.comic.Watch(self.db)

        self.app.add_route('/comics', comic_list)
        self.app.add_route('/comic/{comic_id}', comic)
        self.app.add_route('/watch', watch)

    def run(self):
        httpd = simple_server.make_server('0.0.0.0', 8421, self.app)
        httpd.serve_forever()
