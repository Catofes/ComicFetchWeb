# -*- coding: UTF-8 -*-
from bson.objectid import ObjectId
import RUtils
import re


class ComicList:
    def __init__(self, client):
        self.client = client
        self.db = self.client.comic

    def on_get(self, req, resp):
        data = self.db.comic_list.find({})
        result = []
        for i in data:
            if 'name' in i.keys() and 'update_time' in i.keys():
                result.append({
                    'id': str(i['_id']),
                    'name': i['name'],
                    'update_time': i['update_time'],
                    'mobi': i['mobi'],
                    'mobi_size': i['mobi_size']
                })
        if 'offset' in req.params.keys():
            result = result[int(req.params['offset']):]
        if 'limit' in req.params.keys():
            result = result[0:int(req.params['limit'])]
        req.context['result'] = result


class Comic:
    def __init__(self, client):
        self.client = client
        self.db = self.client.comic

    def on_get(self, req, resp, comic_id):
        comic_data = self.db.comic_list.find_one({'_id': ObjectId(comic_id)})
        if not comic_data:
            raise RUtils.RError(404)
        data = self.db.comic.find({'name': comic_data['name']})
        result = {}
        result['comic'] = {
            'id': str(comic_data['_id']),
            'name': comic_data['name'],
            'update_time': comic_data['update_time'],
            'mobi': i['mobi'],
            'mobi_size': i['mobi_size']
        }
        result['pic'] = []
        for i in data:
            if 'update_time' not in i.keys():
                i['update_time'] = 0
            result['pic'].append({
                'chapter': i['chapter'],
                'pic_num': len(i['pic']),
                'update_time': i['update_time'],
                'next': i['next'],
                'mobi': i['mobi'],
                'mobi_size': i['mobi_size']
            })
        req.context['result'] = result


class Watch:
    def __init__(self, client):
        self.client = client
        self.db = self.client.comic
        self.config = RUtils.RConfig()

    def on_post(self, req, resp):
        if 'request' not in req.context.keys():
            raise RUtils.RError(6)
        request = req.context['request']
        if 'password' not in request.keys():
            raise RUtils.RError(8)
        if request['password'] != self.config.password:
            raise RUtils.RError(9)
        if 'url' not in request.keys():
            raise RUtils.RError(10)
        if not re.match(
                '((http|ftp|https):\/\/)?[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?',
                request['url']):
            raise RUtils.RError(10)
        if not self.db.comic_list.find_one({'url': request['url']}):
            self.db.comic_list.insert({'url': request['url']})
        else:
            raise RUtils.RError(11)
