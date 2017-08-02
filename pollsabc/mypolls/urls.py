from django.conf.urls import include, url
from django.contrib import admin
from views import index,index2,show,showAction


urlpatterns = [
    # Examples:
    # url(r'^$', 'pollsabc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/',index,name="index"),
    url(r'^show/(?P<id>[0-9]+)', show,name="show"),
    url(r'^showAction/(?P<id>[0-9]+)', showAction, name="showAction"),
    url(r'^showResult/(?P<id>[0-9]+)', index2),

]
