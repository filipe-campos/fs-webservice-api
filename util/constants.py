# -*- coding: utf-8 -*-

class Constants:
    def __init__(self):
        #Redis Configuration
        self.REDIS_HOST = 'localhost'
        self.REDIS_PORT = '6379'
        self.REDIS_URL = 'redis://'+self.REDIS_HOST+':'+str(self.REDIS_PORT)

        #Auth URL
        self.AUTH_HOST = 'http://127.0.0.1'
        self.AUTH_PORT = '5001'
        self.AUTH_PATH = '/dashboard/api/v1.0/auth'
        self.AUTH_URL = self.AUTH_HOST+':'+str(self.AUTH_PORT)+self.AUTH_PATH

        self.AUTH_URL_CHECK_TOKEN = self.AUTH_URL+'/token/check'
        self.AUTH_URL_LOGIN = self.AUTH_URL+'/login'
        self.AUTH_URL_CHECK_PASS = self.AUTH_URL+'/password/check'
        self.AUTH_URL_LOGOUT = self.AUTH_URL+'/logout'

        #Core URL's
        self.CORE_HOST = 'http://127.0.0.1'
        self.CORE_PORT = '5002'
        self.CORE_PATH = '/dashboard/api/v1.0'
        self.CORE_URL = self.CORE_HOST+':'+str(self.CORE_PORT)+self.CORE_PATH

        self.CORE_URL_ACC_INSERT = self.CORE_URL+'/account/insert'
        self.CORE_URL_ACC_LIST = self.CORE_URL+'/account/list'
        self.CORE_URL_ACC_DELETE_ALL = self.CORE_URL+'/account/delete/all'
        self.CORE_URL_ACC_RELATIONSHIP_UPDATE = self.CORE_URL+'/account/relationship/update'
        self.CORE_URL_ACC_RELATIONSHIP_CLEAR = self.CORE_URL+'account/relationship/clear'

        self.CORE_URL_ACCOUNTING_RESUME = self.CORE_URL+'/accounting/resume'
        self.CORE_URL_ACCOUNTING_DRE_COMPARATIVE = self.CORE_URL+'/accounting/dre/comparative'
        self.CORE_URL_ACCOUNTING_DRE_MONTH = self.CORE_URL+'/accounting/dre/month'
        self.CORE_URL_ACCOUNTING_DRE_PERIOD = self.CORE_URL+'/accounting/dre/period'
        self.CORE_URL_ACCOUNTING_DRE_ACC_MOV = self.CORE_URL+'/accounting/dre/acc/mov'
        self.CORE_URL_ACCOUNTING_DRE_ACC_MOV_PERIOD = self.CORE_URL+'/accounting/dre/acc/mov/period'

        self.CORE_URL_ACCOUNTING_BAL_COMPARATIVE = self.CORE_URL+'/accounting/balance/comparative'
        self.CORE_URL_ACCOUNTING_BAL_INITIAL_DELETE = self.CORE_URL+'accounting/balance/initial/delete'
        self.CORE_URL_ACCOUNTING_BAL_ACC_BALANCE = self.CORE_URL+'/accounting/balance/acc'

        self.CORE_URL_ACCOUNTING_LAUNCH_LIST = self.CORE_URL+'/accounting/launch/list'
        self.CORE_URL_ACCOUNTING_LAUNCH_LIST_PERIOD = self.CORE_URL+'/accounting/launch/list/period'
        self.CORE_URL_ACCOUNTING_LAUNCH_INSERT = self.CORE_URL+'/accounting/launch/insert'
        self.CORE_URL_ACCOUNTING_LAUNCH_DELETE = self.CORE_URL+'/accounting/launch/delete'

        self.CORE_URL_ACCOUNTING_DFC_MONTH = self.CORE_URL+'/accounting/dfc/month'
        self.CORE_URL_ACCOUNTING_DFC_ACCUMULATED = self.CORE_URL+'/accounting/dfc/accumulated'
        self.CORE_URL_ACCOUNTING_DFC_PROFIT_INSERT = self.CORE_URL+'/accounting/dfc/profit/insert'
        self.CORE_URL_ACCOUNTING_DFC_EXERCISE_INSERT = self.CORE_URL+'accounting/dfc/exercise/insert'
        self.CORE_URL_ACCOUNTING_DFC_INFO_LIST = self.CORE_URL+'/accounting/dfc/info/list'

        self.CORE_URL_ACCOUNTING_EBITDA_PERIOD = self.CORE_URL+'/accounting/ebitda/period'

        self.CORE_URL_ACCOUNTING_INDEX_COMPARATIVE = self.CORE_URL+'/accounting/index/comparative'

        self.CORE_URL_MOVIMENTATION_CALC = self.CORE_URL+'/movimentation/calc'

        self.CORE_URL_COMPANY_INSERT = self.CORE_URL+'/company/insert'
        self.CORE_URL_COMPANY_INFO = self.CORE_URL+'/company/info'
        self.CORE_URL_COMPANY_UPDATE = self.CORE_URL+'/company/update'
        self.CORE_URL_COMPANY_FL_LIST = self.CORE_URL+'/company/file_layout/list'
        self.CORE_URL_COMPANY_FL_INSERT = self.CORE_URL+'/company/file_layout/insert'
        self.CORE_URL_COMPANY_FL_DELETE = self.CORE_URL+'/company/file_layout/delete'

        self.CORE_URL_USER_INSERT = self.CORE_URL+'/user/insert'
        self.CORE_URL_USER_INFO_GET = self.CORE_URL+'/user/get'
        self.CORE_URL_USER_INFO_UPDATE = self.CORE_URL+'/user/update'
        self.CORE_URL_USER_PASS_UPDATE = self.CORE_URL+'/user/password/update'
        self.CORE_URL_USER_COMPANIES_LIST = self.CORE_URL+'/user/companies/list'

        self.CORE_URL_ANALYTIC_ACC_REF_MOV = self.CORE_URL+'/analytic/acc/ref/movimentation'
        self.CORE_URL_ANALYTIC_ACC_REF_BALANCE = self.CORE_URL+'/analytic/acc/ref/balance'
        self.CORE_URL_ANALYTIC_SERIE_LIST = self.CORE_URL+'/analytic/serie/list'
        self.CORE_URL_ANALYTIC_SERIE_DATA_LIST = self.CORE_URL+'/analytic/serie/data/list'
        self.CORE_URL_ANALYTIC_ROI_GET = self.CORE_URL+'/analytic/roi'

        self.CORE_URL_NIKOLE_MSG_LIST = self.CORE_URL+'/nikole/message/list'
        self.CORE_URL_NIKOLE_MSG_READ = self.CORE_URL+'/nikole/message/read'


        #Uploader URL
        self.UPLOADER_HOST = 'http://127.0.0.1'
        self.UPLOADER_PORT = '5003'
        self.UPLOADER_PATH = '/dashboard/api/v1.0/uploader'
        self.UPLOADER_URL = self.UPLOADER_HOST+':'+str(self.UPLOADER_PORT)+self.UPLOADER_PATH

        self.UPLOADER_URL_LAUNCH = self.AUTH_URL+'/launch'
        self.UPLOADER_URL_ACCOUNT = self.AUTH_URL+'/account'
        self.UPLOADER_URL_BALANCE = self.AUTH_URL+'/balance'