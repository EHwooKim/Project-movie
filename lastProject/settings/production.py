from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    # 배포된 url
    '*' #amazon....T T
]
# 헤로쿠 위한 설정
import django_heroku
django_heroku.settings(locals())