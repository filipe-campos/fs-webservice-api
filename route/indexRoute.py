# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('IndexRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()


class IndexRoute:
    
    def get_index_comparative(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            date_start = data['date_start']
            date_end = data['date_end']
        except:
            log.error(inspect.getframeinfo(inspect.currentframe()).function, 
                      str(traceback.format_exc()), 
                      0)
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])
            
        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_ACCOUNTING_INDEX_COMPARATIVE

        return json.dumps(requests.get(url, headers=headers, params=params).json())
       