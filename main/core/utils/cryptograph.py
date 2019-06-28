# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from cryptography.fernet import Fernet
import base64
from django.conf import settings

ENC_KEY = Fernet(settings.SECRET_KEY)


def enc(str):
    return ENC_KEY.encrypt(str.encode('utf-8'))

def dec(str):
    return ENC_KEY.decrypt(str)
