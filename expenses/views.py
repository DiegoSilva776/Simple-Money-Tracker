# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import renderers
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from expenses.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User
from expenses.serializers import UserSerializer
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer


'''
    ROOT
'''
'''
Two things should be noticed here. First, we're using REST framework's reverse function in order 
to return fully-qualified URLs; second, URL patterns are identified by convenience names that we will 
declare later on in our snippets/urls.py.
'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'expenses': reverse('expense-list', request=request, format=format)
    })


'''
    EXPENSES
'''
class ExpenseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        expense = self.get_object()
        return Response(expense.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



'''
    USERS
'''
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
