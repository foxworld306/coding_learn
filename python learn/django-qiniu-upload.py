import os
import uuid
from django.conf import settings
from django.utils.deconstruct import deconstructible
from django.core.files.storage import Storage
from qiniu import Auth, BucketManager, put_data


@deconstructible
class qiniu_upload(Storage):

    def __init__(self, bucket_config=None):
        self.access_key = settings.qiniu_access_key
        self.secret_key = settings.qiniu_secret_key
        self.bucket_name = settings.qiniu_bucket_name
        self.bucket_domain_name = settings.qiniu_bucket_domain.name
        self.private_url = settings.qiniu_private_url
        self._auth = Auth(self.access_key, self.secret_key)
        self._bucket_manager = BucketManager(self._auth)

    
