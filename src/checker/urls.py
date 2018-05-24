from django.conf.urls import url
from . import views

app_name = 'checker'

urlpatterns = [
    url(r'^$',views.question_list,name='question_list'),
    url(r'^(?P<id>[0-9])/ans/$',views.question_ans,name='question_ans_section'),
]
