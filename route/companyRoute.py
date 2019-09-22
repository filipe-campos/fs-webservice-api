# -*- coding: utf-8 -*-
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn

log = Log('CompanyRoute')
util = Util()
constants = Constants()
codeReturn = CodeReturn()

class CompanyRoute:

    def get_company_info(self, request):
        try:
            header = request.headers

            # Get Token from Header
            token = str(header['token'])
            # Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            company_token = data['company_token']
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

        url = constants.CORE_URL_COMPANY_INFO

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def update_company_info(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                # Get Token from Header
                token = str(header['token'])
                # Get datas from JSON
                data = json.loads(str(content['data']).replace("'", '"'))

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

            url = constants.CORE_URL_COMPANY_UPDATE

            return json.dumps(requests.put(url, headers=headers, data=json.dumps(payload)).json())

        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def insert_company(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                # Get Token from Header
                token = str(header['token'])
                # Get datas from JSON
                data = json.loads(str(content['data']).replace("'", '"'))
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

            url = constants.CORE_URL_COMPANY_INSERT

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())

        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    ## -- FILE LAYOUT -- ##
    def list_file_layout(self, request):
        try:
            header = request.headers

            # Get Token from Header
            token = str(header['token'])
            # Get datas from PARAMS
            data = json.loads(str(request.args.get('data')).replace("'", '"'))

            company_token = data['company_token']
            import_type = data['import_type']
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        params = {
            'data':json.dumps(data)
        }

        url = constants.CORE_URL_COMPANY_FL_LIST

        return json.dumps(requests.get(url, headers=headers, params=params).json())

    def insert_file_layout(self, request):
        if (request.is_json):
            try:
                content = request.get_json()
                header = request.headers

                # Get Token from Header
                token = str(header['token'])
                # Get datas from JSON
                data = json.loads(str(content['data']).replace("'", '"'))

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

            url = constants.CORE_URL_COMPANY_FL_INSERT

            return json.dumps(requests.post(url, headers=headers, data=json.dumps(payload)).json())

        else:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

    def delete_file_layout(self, request):
        try:
            content = request.get_json()
            header = request.headers

            # Get Token from Header
            token = str(header['token'])
            # Get datas from JSON
            data = json.loads(str(content['data']).replace("'", '"'))

            layout_id = data['layout_id']
        except:
            log.error(inspect.getframeinfo(inspect.currentframe()).function, 
                      str(traceback.format_exc()), 
                      0)

            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        payload = {
            'data':data
        }

        url = constants.CORE_URL_COMPANY_FL_DELETE

        return json.dumps(requests.delete(url, headers=headers, data=json.dumps(payload)).json())