# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from expenses.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User
from expenses.serializers import UserSerializer
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer


'''
   Set the view of the class ExpenseList as the ListCreateAPIView, 
   * which use the mixins provided by the DjangoREST framework,
   * which uses the APIView class that encapsulates the behaviour of the Request and Response objects,
   * which make it easier to handle the format of the Response to the user, for example by identifying 
   the content type and sending the correct representation of the data. 
   For instance: lets say HTML to display in a browser, or JSON for an Ajax request
'''
class ExpenseList(generics.ListCreateAPIView):
    # Set the search universe for the generic ListCreateAPIView class and the serializer class
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    # Add a property that determines the minimun Authentication requirements to access objects of the Expense class
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # Overwrite the create method of the generic APIView class, in order to set the owner attribute as the
    # User object that was passed within the Request object
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    # Add a property that determines the minimun Authentication requirements to access objects of the Expense class
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
