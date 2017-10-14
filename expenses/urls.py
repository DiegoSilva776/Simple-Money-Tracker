from django.conf.urls import url
from django.conf.urls import include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from expenses.views import ExpenseViewSet, UserViewSet, api_root


# Explicitly create the ViewSets
expense_list = ExpenseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
expense_detail = ExpenseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
expense_highlight = ExpenseViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


# Allow passing the content type at the end of the Request url and name all endpoints but the root
urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^expenses/$', expense_list, name='expense-list'),
    url(r'^expenses/(?P<pk>[0-9]+)/$', expense_detail, name='expense-detail'),
    url(r'^expenses/(?P<pk>[0-9]+)/highlight/$', expense_highlight, name='expense-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
])

# Add the default login and logout endpoints from the DjangoREST framework to the app
# The r'^api-auth/' part of pattern can actually be whatever URL you want to use. 
# The only restriction is that the included urls must use the 'rest_framework' namespace.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
