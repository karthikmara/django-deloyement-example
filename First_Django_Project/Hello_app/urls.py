from django.conf.urls import url
from Hello_app import views


urlpatterns=[
    url(r'^$',views.index,name='index'),
]
