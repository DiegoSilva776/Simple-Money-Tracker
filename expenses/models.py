# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

class Expense(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    value = models.DecimalField(0, max_digits=20, decimal_places=2)
    
    class Meta:
        ordering = ('created',)
