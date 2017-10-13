from django.conf.urls import url
from expenses import views

urlpatterns = [
    url(r'^expenses/$', views.expenses_list),
    url(r'^expenses/(?P<pk>[0-9]+)/$', views.expense_detail),
]
