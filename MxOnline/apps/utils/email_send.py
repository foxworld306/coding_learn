# -*- coding: utf-8 -*-

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "鎱曞鍦ㄧ嚎缃戞敞鍐屾縺娲婚摼鎺�"
        email_body = "璇风偣鍑讳笅闈㈢殑閾炬帴婵�娲讳綘鐨勮处鍙�: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "鎱曞鍦ㄧ嚎缃戞敞鍐屽瘑鐮侀噸缃摼鎺�"
        email_body = "璇风偣鍑讳笅闈㈢殑閾炬帴閲嶇疆瀵嗙爜: http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "鎱曞鍦ㄧ嚎閭淇敼楠岃瘉鐮�"
        email_body = "浣犵殑閭楠岃瘉鐮佷负: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


