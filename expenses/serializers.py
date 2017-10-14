from django.contrib.auth.models import User
from rest_framework import serializers
from expenses.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    # We could have also used CharField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Expense
        fields = ('id', 'title', 'code', 'value', 'owner')


class UserSerializer(serializers.ModelSerializer):
    expenses = serializers.PrimaryKeyRelatedField(many=True, queryset=Expense.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'expenses')

