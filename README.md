## ComicFetchWeb

This is the web backend of ComicFetch to show comics.

You need python3 pymongo falcon

### APIs

#### Get Comic Lists:

GET: /comics?limit=xxx&offset=xxx

RETURN: `[{'name': comic_name, 'id': comic_id, 'update_time': time in UTC}]`

EXAMPLE:

```
GET: /comics?limit=2

RETURNS:

[{"name": "\u52c7\u8005\u6b7b\u4e86\uff01\u662f\u56e0\u4e3a\u52c7\u8005\u6389\u8fdb\u4e86\u4f5c\u4e3a\u6751\u6c11\u7684\u6211\u6316\u7684\u9677\u9631\u91cc", "id": "56cd30b5bb5f6be255694e61", "update_time": 1456296552.5513806}, {"name": "\u6211\u5bb6\u5927\u5e08\u5144\u8111\u5b50\u6709\u5751", "id": "56cd37f684df9b63e6901a59", "update_time": 1456296613.2351563}]
```

#### Get Comic

GET: /comic/{comic_id}

RETURN:    `[{"pic_num": the number of pictures in this chapter, "chapter": chapter name}]`

EXAMPLE:
```
GET :/comic/56cd30b5bb5f6be255694e61/

RETURNS:
[{"pic_size": 26, "chapter": "\u7b2c01\u8bdd"}, {"pic_size": 21, "chapter": "\u7b2c23\u8bdd"}, {"pic_size": 22, "chapter": "\u7b2c05\u8bdd"}, {"pic_size": 21, "chapter": "\u7b2c26\u8bdd"}, {"pic_size": 24, "chapter": "\u7b2c02\u8bdd"}, {"pic_size": 19, "chapter": "\u7b2c46\u8bdd"}, {"pic_size": 14, "chapter": "\u7b2c22\u8bdd"}, {"pic_size": 20, "chapter": "\u7b2c30\u8bdd"}, {"pic_size": 16, "chapter": "\u7b2c27\u8bdd\u2460"}, {"pic_size": 18, "chapter": "\u7b2c47\u8bdd"}, {"pic_size": 17, "chapter": "\u7b2c40\u8bdd"}, {"pic_size": 21, "chapter": "\u7b2c17\u8bdd"}, {"pic_size": 6, "chapter": "\u756a\u5916\u7bc706"}, {"pic_size": 23, "chapter": "\u7b2c34\u8bdd"}, {"pic_size": 4, "chapter": "\u756a\u5916\u7bc72"}, {"pic_size": 16, "chapter": "\u7b2c15\u8bdd"}, {"pic_size": 16, "chapter": "\u7b2c19\u8bdd"}, {"pic_size": 23, "chapter": "\u7b2c28\u8bdd"}, {"pic_size": 16, "chapter": "\u7b2c16\u8bdd"}, {"pic_size": 19, "chapter": "\u7b2c49\u8bdd"}, {"pic_size": 5, "chapter": "\u756a\u5916\u7bc705"}, {"pic_size": 16, "chapter": "\u7b2c14\u8bdd"}, {"pic_size": 21, "chapter": "\u7b2c36\u8bdd"}, {"pic_size": 18, "chapter": "\u7b2c11\u8bdd"}, {"pic_size": 14, "chapter": "\u7b2c47\u8bdd\u2461"}, {"pic_size": 22, "chapter": "\u7b2c06\u8bdd"}, {"pic_size": 3, "chapter": "\u756a\u5916\u7bc71"}, {"pic_size": 17, "chapter": "\u7b2c32\u8bdd"}, {"pic_size": 16, "chapter": "\u7b2c33\u8bdd"}, {"pic_size": 25, "chapter": "\u7b2c10\u8bdd"}, {"pic_size": 18, "chapter": "\u7b2c25\u8bdd"}, {"pic_size": 20, "chapter": "\u7b2c42\u8bdd"}, {"pic_size": 19, "chapter": "\u7b2c43\u8bdd"}, {"pic_size": 23, "chapter": "\u7b2c24\u8bdd"}, {"pic_size": 19, "chapter": "\u7b2c48\u8bdd"}, {"pic_size": 15, "chapter": "\u7b2c20\u8bdd"}, {"pic_size": 20, "chapter": "\u7b2c45\u8bdd"}, {"pic_size": 13, "chapter": "\u7b2c27\u8bdd\u2461"}, {"pic_size": 16, "chapter": "\u7b2c18\u8bdd"}, {"pic_size": 15, "chapter": "\u7b2c35\u8bdd"}, {"pic_size": 17, "chapter": "\u7b2c39\u8bdd"}, {"pic_size": 6, "chapter": "\u756a\u5916\u7bc74"}, {"pic_size": 31, "chapter": "\u9644\u5f5501-22\u8bdd"}, {"pic_size": 16, "chapter": "\u7b2c38\u8bdd"}, {"pic_size": 18, "chapter": "\u7b2c41\u8bdd"}, {"pic_size": 18, "chapter": "\u7b2c07\u8bdd"}, {"pic_size": 15, "chapter": "\u7b2c31\u8bdd"}, {"pic_size": 23, "chapter": "\u7b2c03\u8bdd"}, {"pic_size": 17, "chapter": "\u7b2c09\u8bdd"}, {"pic_size": 21, "chapter": "\u7b2c29\u8bdd"}, {"pic_size": 7, "chapter": "03\u5377\u756a\u5916"}, {"pic_size": 17, "chapter": "\u7b2c44\u8bdd"}, {"pic_size": 13, "chapter": "\u7b2c35\u8bdd\u2461"}, {"pic_size": 5, "chapter": "\u756a\u5916\u7bc73"}, {"pic_size": 11, "chapter": "\u7b2c49\u8bdd2"}, {"pic_size": 14, "chapter": "\u7b2c13\u8bdd"}, {"pic_size": 16, "chapter": "\u7b2c21\u8bdd"}, {"pic_size": 16, "chapter": "\u7b2c37\u8bdd"}, {"pic_size": 21, "chapter": "\u7b2c04\u8bdd"}, {"pic_size": 15, "chapter": "\u7b2c08\u8bdd"}, {"pic_size": 14, "chapter": "\u7b2c12\u8bdd"}]
```

#### Watch

POST: /watch/

BODY:
```
{'password':password,'url':url}
```

A API that add comic to be watched. Pass the dmzj.com's URL to pyspider.
You should set `Content-Type: application/json; charset=utf-8` in your request header.


