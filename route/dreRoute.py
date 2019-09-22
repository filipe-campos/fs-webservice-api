# -*- coding: utf-8 -*-
import json
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('DRERoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()


class DRERoute:
    
    def get_dre_comparative(self, request):
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

        url = constants.CORE_URL_ACCOUNTING_DRE_COMPARATIVE

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def get_dre_month(self, request):
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

        url = constants.CORE_URL_ACCOUNTING_DRE_MONTH

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def get_dre_period(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            date_start1 = data['date_start1']
            date_end1 = data['date_end1']
            date_start2 = data['date_start2']
            date_end2 = data['date_end2']
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_ACCOUNTING_DRE_PERIOD

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def list_acc_mov_from_acc_ref(self, request):
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

        url = constants.CORE_URL_ACCOUNTING_DRE_ACC_MOV

        return json.dumps(requests.get(url, headers=headers, params=params).json())
    
    def list_acc_mov_from_acc_ref_period(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from JSON
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            date_start1 = data['date_start1']
            date_end1 = data['date_end1']
            date_start2 = data['date_start2']
            date_end2 = data['date_end2']
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

        url = constants.CORE_URL_ACCOUNTING_DRE_ACC_MOV_PERIOD

        return json.dumps(requests.get(url, headers=headers, params=params).json())
