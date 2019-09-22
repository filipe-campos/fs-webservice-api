# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('LaunchRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()


class LaunchRoute:
    
    def list_launch(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            date = data['date']
            cod_account = data['cod_account']
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_ACCOUNTING_LAUNCH_LIST

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def list_launch_period(self, request):
        try:
            header = request.headers

            #Get Token from Header
            token = str(header['token'])
            #Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            companies_token = data['companies_token']
            date_start = data['date_start']
            date_end = data['date_end']
            cod_account = data['cod_account']
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_ACCOUNTING_LAUNCH_LIST_PERIOD
        
        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def insert_launch(self, request):
        if request.is_json:
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from JSON
                data = json.loads(str(content['data']).replace("'",'"'))

                company_token = data['company_token']

                launch_list = data['launch_list']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
            'Content-Type': 'application/json',
            'token': token
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_ACCOUNTING_LAUNCH_INSERT

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def delete_launch(self, request):
        try:
            content = request.get_json()
            header = request.headers

            #Get Token from Header
            token = str(header['token'])

            #Get datas from JSON
            data = json.loads(str(content['data']).replace("'",'"'))
            
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

        url = constants.CORE_URL_ACC_DELETE_ALL

        return json.dumps(requests.delete(url, headers=headers, data=json.dumps(payload)).json())
