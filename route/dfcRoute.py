# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('DFCRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()

class DFCRoute:
    
    def get_dfc(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            date = data['date']
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

        url = constants.CORE_URL_ACCOUNTING_DFC_MONTH

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def get_dfc_accumulated(self, request):
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
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_ACCOUNTING_DFC_ACCUMULATED

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def insert_dfc_profit(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from PARAMS
                data = json.loads(str(content['data']).replace("'",'"'))

                company_token = data['company_token']
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

            url = constants.CORE_URL_ACCOUNTING_DFC_PROFIT_INSERT

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())   
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])
    
    def insert_dfc_exercise(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from PARAMS
                data = json.loads(str(content['data']).replace("'",'"'))

                company_token = data['company_token']
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

            url = constants.CORE_URL_ACCOUNTING_DFC_EXERCISE_INSERT

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())    
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])
    
    def list_dfc_info(self, request):
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

        url = constants.CORE_URL_ACCOUNTING_DFC_INFO_LIST

        return json.dumps(requests.get(url, headers=headers, params=params).json())   
  