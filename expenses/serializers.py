from django.contrib.auth.models import User
from rest_framework import serializers
from expenses.models import Expense


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    # We could have also used CharField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='expense-highlight', format='html')

    class Meta:
        model = Expense
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'category', 'value')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    expenses = serializers.HyperlinkedRelatedField(many=True, view_name='expense-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'expenses')
