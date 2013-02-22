# -*- coding: utf-8 -*-

import json
import logging
from google.appengine.api import urlfetch

from application.utils import const


def search(author_id=None, category_id=None, tags=None):
    request = {
        "substance": {
            "author_id": author_id,
            "category_id": category_id,
            "tags": tags,
        }
    }
    data = json.dumps(request)
    url = const.WEB_SERVICE_URL_KIT_SEARCH
    ret = _execute_service_post(url, data)
    if ret and ret.get("response").get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
        return ret.get("response").get("substance").get("items")
    else:
        return None


def read(kit_id):
    url = const.WEB_SERVICE_URL_KIT_READ + kit_id
    ret = _execute_service_get(url)
    if ret and ret.get("response").get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
        return ret.get("response").get("substance")
    else:
        return None


def _execute_service_get(url):
    try:
        res = urlfetch.fetch(url=url, deadline=10)
        if res.status_code == 200:
            return json.loads(res.content, "utf-8")
    except Exception, ex:
        logging.error(ex.message)
    return None


def _execute_service_post(url, data):
    try:
        method = urlfetch.POST
        headers = {"Content-Type": "application/json"}
        res = urlfetch.fetch(url=url, payload=data, method=method, headers=headers, deadline=10)
        if res.status_code == 200:
            return json.loads(res.content, "utf-8")
    except Exception, ex:
        logging.error(ex.message)
    return None














