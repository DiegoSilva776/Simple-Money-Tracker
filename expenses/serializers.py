from rest_framework import serializers
from expenses.models import Expense, LANGUAGE_CHOICES, STYLE_CHOICES


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'title', 'code')
