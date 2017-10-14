# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer
from rest_framework import generics

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


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    # Set the search universe for the generic ListCreateAPIView class and the serializer class
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

