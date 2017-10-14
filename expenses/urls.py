from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from expenses import views

urlpatterns = [
    url(r'^expenses/$', views.ExpenseList.as_view()),
    url(r'^expenses/(?P<pk>[0-9]+)/$', views.ExpenseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
