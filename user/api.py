# from django.shortcuts import render
#
# # Create your views here.
#
# from django.core.cache import cache

from lib.http import render_json
from lib.sms import send_sms
# from common import keys
# from common import errors
# from user.models import User


def submit_phone(request):
    '''提交手机号，发送验证码'''
    phone = request.POST.get('phone')
    # phone = request.GET.get('phone')
    print(phone)
    send_sms(phone)
    data={
        "status":200,
        "msg":"ok"
    }
    return render_json(data)