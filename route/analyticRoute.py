# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from datetime import datetime 
from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('AnalyticRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()

class AnalyticRoute:
    
    def list_acc_ref_movimentation(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            classification_ref = data['classification_ref']
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

        url = constants.CORE_URL_ANALYTIC_ACC_REF_MOV

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def list_acc_ref_balance(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            classification_ref = data['classification_ref']
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

        url = constants.CORE_URL_ANALYTIC_ACC_REF_BALANCE

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def list_serie(self, request):
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

        url = constants.CORE_URL_ANALYTIC_SERIE_LIST

        return json.dumps(requests.get(url, headers=headers).json())

    def list_serie_data(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            serie_type_id = data['serie_type_id']
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

        url = constants.CORE_URL_ANALYTIC_SERIE_DATA_LIST

        return json.dumps(requests.get(url, headers=headers, params=params).json())
    
    def get_roi(self, request):
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

        url = constants.CORE_URL_ANALYTIC_ROI_GET

        return json.dumps(requests.get(url, headers=headers, params=params).json())