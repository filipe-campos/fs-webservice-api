# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('MovimentationRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()

class MovimentationRoute:
    
    def calc_movimentation(self, request):
        try:
            content = request.get_json()
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from JSON
            data = json.loads(str(content['data']).replace("'",'"'))

            company_token = data['company_token']
            date = data['date']
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        payload = {
            'data':data
        }

        url = constants.CORE_URL_MOVIMENTATION_CALC

        return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())