# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('NikoleRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()

class NikoleRoute:
    
    def list_message(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])         

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_NIKOLE_MSG_LIST

        return json.dumps(requests.get(url, headers=headers, params=params).json())


    def read_message(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from PARAMS
                data = json.loads(str(content['data']).replace("'",'"'))

                msg_id = data['msg_id']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
                'Content-Type': 'application/json',
                'token': token
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_NIKOLE_MSG_READ

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())

    