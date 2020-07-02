from flask import g, Response, request
import re
import hashlib
import json
from datetime import datetime
class Database(object):

    def __init__(self,**kwargs):
        self.no_hp = kwargs.get('no_hp','')
        self.email = kwargs.get('email', '')
        self.cursor = g.cursor
        self.lang = 'en-us'

        #balesan respon
        self.payload = dict(
            error_code=0,
            results={},
            meta={},
            resp_message=''
        )

    def get_user_info(self):
        '''method untuk cek user dari no_hp dan email'''

        query = '''
        select * from user_mit where mobile = %s or email = %s
        '''

        result = self.cursor(query,[self.no_hp,self.email])

        #jika ada, berarti tidak unique
        print(result.rowcount)
        if result.rowcount>0:
            self.payload['error_code']=210
            return self.payload

        self.payload['results'] = 'user_unique'
        return self.payload

    def save_register(self,f_name,l_name,birth,gender):
        '''method untuk menyimpan register data'''

        query = '''
        INSERT INTO user_mit (mobile, first_name, last_name, birth, gender, email) 
        VALUES (%s, %s, %s, %s, %s, %s);
        '''

        result = self.cursor(query,[self.no_hp,f_name,l_name,birth,gender,self.email])

        if not result.rowcount:
            self.payload['error_code']=204
            return self.payload
        
        self.payload['results'] = 'register success'
        return self.payload

    def login(self):
        '''method untuk login dengan no_hp atau email'''
        query = '''
        select * from user_mit where mobile = %s and email = %s
        '''

        result = self.cursor(query,[self.no_hp,self.email])

        #jika tidak ada, belum mendaftar
        if result.rowcount==0:
            self.payload['error_code']=204
            return self.payload

        self.payload['results'] = 'login successfull'
        return self.payload
        