# -*- coding: utf-8 -*-
import json
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('AuthRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()

class AuthRoute:
    
    def login(self, request):
        if (request.is_json):
            try:
                content = request.get_json()

                #Get datas from JSON
                user = str(content['user'])
                password = str(content['pass'])
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
                'Content-Type': 'application/json',
            }

            payload = {
                'user':user,
                'pass': password
            }

            url = constants.AUTH_URL_LOGIN

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())

        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def check_password(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from JSON
                data = json.loads(str(content['data']).replace("'",'"'))

                password = data['pass']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
                'Content-Type': 'application/json',
                'token': token
            }

            payload = {
                'data':data
            }

            url = constants.AUTH_URL_CHECK_PASS

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())   
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def logout(self, request):
        json_data = {}

        if request.is_json:
            header = request.headers

            #Get datas from JSON
            #token = str(header['token'])

        return json_data
