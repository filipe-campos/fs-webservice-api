# -*- coding: utf-8 -*-
import os
import json
import traceback
import inspect
import requests

from flask import Flask, request
from util import Util, Constants, Log, CodeReturn

log = Log('AccountingRoute')
util = Util()
constants = Constants()
codeReturn = CodeReturn()

class AccountingRoute:

    def get_resume(self, request):
        try:
            header = request.headers

            # Get Token from Header
            token = str(header['token'])
            # Get datas from PARAMS
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

        url = constants.CORE_URL_ACCOUNTING_RESUME

        return json.dumps(requests.get(url, headers=headers, params=params).json())
