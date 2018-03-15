# coding=utf-8

import os
import uuid
from django.conf import settings
from django.utils.deconstruct import deconstructible
from django.core.files.storage import Storage, File
from qiniu import Auth, BucketManager, put_data
from django.core.exceptions import ImproperlyConfigured, SuspiciousOperation
from django.utils.encoding import force_text, force_bytes, filepath_to_uri

@deconstructible
class QiniuCloud(Storage):

    def __init__(self, qiniuconfig=None):
        if not qiniuconfig:
            qiniuconfig = settings.QINIU_CONFIG

        self.access_key = qiniuconfig['qiniu_access_key']
        self.secret_key = qiniuconfig['qiniu_secret_key']
        self.bucket_name = qiniuconfig['qiniu_bucket_name']
        self.bucket_domain_name = qiniuconfig['qiniu_bucket_domain_name']
        self.secure_url = qiniuconfig['qiniu_secure_url']
        self._auth = Auth(self.access_key, self.secret_key)
        self._bucket_manager = BucketManager(self._auth)

    def open(self, name, mode='rb'):
        return self._open(name, mode)


    def save(self, name, content, max_length=None):
        if name is None:
            name = content.name

        if hasattr(content, 'chunks'):
            content_str = b''.join(chunk for chunk in content.chunks())
        else:
            content_str = content.read()

        self.upload_data(name, content_str)
        return name

    def upload_data(self, name, content):
        token = self.auth.upload_token(self.bucket_name)
        ret, info = put_data(token, name, content)
        if ret.get('key', None) == None:
            raise Exception('Upload Error')


            # self.access_key = settings.qiniu_access_key
            # self.secret_key = settings.qiniu_secret_key
            # self.bucket_name = settings.qiniu_bucket_name
            # self.bucket_domain_name = settings.qiniu_bucket_domain.name
            # self.private_url = settings.qiniu_private_url
            # self._auth = Auth(self.access_key, self.secret_key)
            # self._bucket_manager = BucketManager(self._auth)


# @deconstructible
# class Qiniu_Config(Storage):
#
#     def __init__(self,
#             access_key=QINIU_AK,
#             secret_key=QINIU_SK,
#             bucket_name=QINIU_BUCKET_NAME,
#             bucket_domain=QINIU_BUCKET_DOMAIN_NAME,
#             secure_url=QINIU_SECURE_URL):
#         self.auth = Auth(access_key, secret_key)
#         self.bucket_name = bucket_name
#         self.bucket_domain = bucket_domain
#         self.bucket_manager = BucketManager(self.auth)
#         self.secure_url = secure_url