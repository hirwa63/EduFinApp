from rest_framework import serializers
from core.models import Testing

class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'

class TestingNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = ['id', 'name'] 
        from core.models import Testing, Transaction, Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'name', 'limit_amount', 'month']
        read_only_fields = ['id', 'user']