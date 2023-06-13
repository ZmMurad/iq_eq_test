from django.urls import include, path
from core.views import IQ_API, EQ_API, Login_API, get_login_test

urlpatterns = [
    path("login/", Login_API.as_view(),name="login"),
    path("iq_post/",IQ_API.as_view(),name="iq_post"),
    path('eq_post/',EQ_API.as_view(),name="eq_post"),
    path("get_test/",get_login_test,name="get_test")
]
