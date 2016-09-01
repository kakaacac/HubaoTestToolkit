# -*- coding: utf-8 -*-
import time
import hmac
import hashlib
import base64
import json
import requests
import re

class Requester(object):
    APP_KEY = '744674fe-e71b-5a35-acac-bb7f0a49e627'
    APP_SECRET = '8ed0e31b7db840b7bf539ed7d5e86f94'

    def __init__(self, user_id=None, udid=None, access_token=None, app_secret=None):
        self.user_id = user_id
        self.udid = udid
        self.access_token = access_token
        self.app_secret = app_secret or self.APP_SECRET
        self.app_key = self.APP_KEY

    def generate_visitor_auth(self):
        timestamp = str(time.time())
        certs = hmac.new(str(self.app_secret), self.udid+timestamp, hashlib.sha1).hexdigest()
        data = self.app_key + '-' + self.udid + ':' + certs + '.' + timestamp
        return base64.b64encode(data)

    def generate_user_auth(self):
        timestamp = str(time.time())
        certs = hmac.new(str(self.access_token), self.udid+timestamp, hashlib.sha1).hexdigest()
        data = self.app_key + '.' + self.user_id + ':' + certs + '.' + timestamp
        return base64.b64encode(data)

    def get_header(self, content_type="application/x-www-form-urlencoded", visitor=False):
        if visitor:
            return {
                'Content-Type': content_type,
                'Authorization': 'Basic ' + self.generate_visitor_auth()
            }

        return {
            'Content-Type': content_type,
            'Authorization': 'Basic ' + self.generate_user_auth()
        }

    def request(self, url, method="get", data=None, content_type="application/x-www-form-urlencoded", visitor=False):
        assert method in ("get", "post", "put", "delete")
        header = self.get_header(content_type, visitor)
        body_data, json_data = (None, data) if content_type == "application/json" else (data, None)

        try:
            if method == "get":
                response = requests.get(url, data, headers=header)
            elif method == "post":
                response = requests.post(url, body_data, json_data, headers=header)
            elif method == "put":
                response = requests.put(url, data, headers=header)
            else:
                response = requests.delete(url, headers=header)
        except Exception as e:
            raise

        return {
            "status": response.status_code,
            "content": json.dumps(json.loads(response.content), ensure_ascii=False, indent=2)
        }


