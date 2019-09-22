# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('UserRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()

class UserRoute:
    
    def insert_user(self, request):
        if (request.is_json):
            content = request.get_json()

            try:
                #Get datas from JSON 
                data = json.loads(str(content['data']).replace("'", '"'))

                info = data['info']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])
 
            headers = {
                'Content-Type': 'application/json'
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_USER_INSERT

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())
                    
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def get_user_info(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
        except:
           return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, []) 

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_USER_INFO_GET

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def update_user_info(self, request):
        if (request.is_json):
            content = request.get_json()
            header = request.headers

            try:
                #Get Token from Header
                token = str(header['token'])
                #Get datas from JSON
                data = json.loads(str(content['data']).replace("'",'"'))

                info = data['info']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
            'Content-Type': 'application/json',
            'token': token
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_USER_INFO_UPDATE

            return json.dumps(requests.put(url, headers=headers, data=json.dumps(payload)).json())
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def update_user_pass(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from JSON
                data = json.loads(str(content['data']).replace("'",'"'))

                old_password = data['old_password']
                new_password = data['new_password']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])
            
            headers = {
            'Content-Type': 'application/json',
            'token': token
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_USER_PASS_UPDATE

            return json.dumps(requests.put(url, headers=headers, data=json.dumps(payload)).json())
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def list_user_companies(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
        except:
           return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, []) 

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        url = constants.CORE_URL_USER_COMPANIES_LIST

        return json.dumps(requests.get(url, headers=headers).json())
