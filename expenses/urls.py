from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from expenses import views

urlpatterns = [
    url(r'^expenses/$', views.ExpenseList.as_view()),
    url(r'^expenses/(?P<pk>[0-9]+)/$', views.ExpenseDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

# Allow to pass the content type at the end of the Request url
urlpatterns = format_suffix_patterns(urlpatterns)

# Add the default login and logout endpoints from the DjangoREST framework to the app
# The r'^api-auth/' part of pattern can actually be whatever URL you want to use. 
# The only restriction is that the included urls must use the 'rest_framework' namespace.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
