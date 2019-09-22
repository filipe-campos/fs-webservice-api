# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn

log = Log('AccountRoute')
util = Util()
constants = Constants()
codeReturn = CodeReturn()

class AccountRoute:

    def list_account(self, request):
        try:
            content = request.get_json()
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

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_ACC_LIST

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def insert_account(self, request):
        if request.is_json:
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from JSON
                data = json.loads(str(content['data']).replace("'",'"'))

                company_token = data['company_token']
                
                if ('account_list' not in data) and ('account' not in data):
                    return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
            'Content-Type': 'application/json',
            'token': token
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_ACC_INSERT

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])


    def delete_all_account(self, request):
        if request.is_json:
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
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])


    def update_acc_relationship(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                #Get Token from Header
                token = str(header['token'])
                #Get datas from JSON
                data = json.loads(str(content['data']).replace("'",'"'))

                company_token = data['company_token']
                cod_account = data['cod_account']
                classification_ref = data['classification_ref']
            except:
                return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

            headers = {
            'Content-Type': 'application/json',
            'token': token
            }

            payload = {
                'data':data
            }

            url = constants.CORE_URL_ACC_RELATIONSHIP_UPDATE

            return json.dumps(requests.put(url, headers=headers, data=json.dumps(payload)).json())
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def clear_acc_relationship(self, request):
        if (request.is_json):
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

            url = constants.CORE_URL_ACC_RELATIONSHIP_CLEAR

            return json.dumps(requests.put(url, headers=headers, data=json.dumps(payload)).json())        
        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])