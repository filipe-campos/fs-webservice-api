# -*- coding: utf-8 -*-
import os
import json
import asyncio 
import traceback
import inspect
import requests

from flask import Flask, request
from flask import send_file, send_from_directory
from werkzeug.utils import secure_filename
from util import Util, Constants, Log, CodeReturn
from controller import Controller

log = Log('UploadRoute')
util = Util()
constants = Constants()
controller = Controller()
codeReturn = CodeReturn()

class UploadRoute:
     
    def upload_launchs(self, request):
        try:
            content = request.get_json()
            header = request.headers

            #Get Token from Header
            token = str(header['token'])   

            data = request.form.to_dict()

            date = request.form.to_dict()['date']
            layout_id = request.form.to_dict()['layout_id']
            company_token = request.form.to_dict()['company_token']
            file = request.files['file'] 
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        url = constants.UPLOADER_URL_LAUNCH

        return json.dumps(requests.post(url, headers=headers, files=file, data=data).json())

    def upload_account(self, request):
        try:
            content = request.get_json()
            header = request.headers

            #Get Token from Header
            token = str(header['token'])   

            data = request.form.to_dict()

            layout_id = request.form.to_dict()['layout_id']
            company_token = request.form.to_dict()['company_token']
            file = request.files['file'] 
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        url = constants.UPLOADER_URL_ACCOUNT

        return json.dumps(requests.post(url, headers=headers, files=file, data=data).json())


    def upload_balance(self, request):
        try:
            content = request.get_json()
            header = request.headers

            #Get Token from Header
            token = str(header['token'])   

            data = request.form.to_dict()

            date = request.form.to_dict()['date']
            layout_id = request.form.to_dict()['layout_id']
            company_token = request.form.to_dict()['company_token']
            file = request.files['file'] 
        except:
            return util.make_json(codeReturn.BAD_REQUEST_CODE, codeReturn.BAD_REQUEST_MSG, [])

        headers = {
            'Content-Type': 'application/json',
            'token': token
        }

        url = constants.UPLOADER_URL_BALANCE

        return json.dumps(requests.post(url, headers=headers, files=file, data=data).json())