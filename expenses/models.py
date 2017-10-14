# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

class Expense(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    value = models.DecimalField(0, max_digits=20, decimal_places=2)
    highlighted = models.TextField()

    # Relationships
    owner = models.ForeignKey('auth.User', related_name='expenses', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Always make the first letter of the title uppercase
        """
        # Modify the title appearance
        self.title = self.title.capitalize()

        # Create a highlighted version of the object
        self.highlighted = 'Despesa %s : %f' % (self.title, self.value)

        super(Expense, self).save(*args, **kwargs)
