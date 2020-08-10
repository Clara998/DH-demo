from django.urls import path

from . import views
from . import handler

app_name = 'dh'

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('gen_p',handler.gen_p_handler, name='gen_p'),
    path('gen_a',handler.gen_a_handler, name='gen_a'),
    path('show_encode',handler.show_encode_handler, name='show_encode'),
    path('show_decode',handler.show_decode_handler, name='show_decode')
]