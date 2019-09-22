# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn

log = Log('BalanceRoute')
util = Util()
constants = Constants()
codeReturn = CodeReturn()

class BalanceRoute:
    
    def get_balance(self, request):
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

        url = constants.CORE_URL_ACCOUNTING_BAL_COMPARATIVE

        return json.dumps(requests.get(url, headers=headers, params=params).json())
    
    def delete_balance(self, request):
        if request.is_json:
            try:
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from PARAMS
                data = json.loads(str(request.args.get('data')).replace("'", '"'))

                company_token = data['company_token']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
            'Content-Type': 'application/json',
            'token': token
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_ACCOUNTING_BAL_INITIAL_DELETE

            return json.dumps(requests.delete(url, headers=headers, data=json.dumps(payload)).json())

        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def list_acc_balance_comparative(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from JSON
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            date_start = data['date_start']
            date_end = data['date_end']
            cod_account_ref = data['cod_account_ref']
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_ACCOUNTING_BAL_ACC_BALANCE

        return json.dumps(requests.get(url, headers=headers, params=params).json())
