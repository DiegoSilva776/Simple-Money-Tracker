# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer
from rest_framework import mixins
from rest_framework import generics

class ExpenseList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    # Set the space in which the mixin class is going to search for results
    queryset = Expense.objects.all()

    # Set the serializer class for the mixin class
    serializer_class = ExpenseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ExpenseDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    # Set the space in which the mixin class is going to search for results
    queryset = Expense.objects.all()

    # Set the serializer class for the mixin class
    serializer_class = ExpenseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

