from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Testing, Transaction, Budget
from core.serializers import TestingSerializer, TransactionSerializer, BudgetSerializer


# --- Existing views from Lab 1 ---

def testing_view(request):
    data = Testing.objects.all()
    serializer = TestingSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def health_check(request):
    return JsonResponse({'status': 'ok'})

def testing_detail_view(request, id):
    try:
        testing = Testing.objects.get(id=id)
        serializer = TestingSerializer(testing)
        return JsonResponse(serializer.data)
    except Testing.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)


# --- Transaction CRUD views ---

class TransactionListView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            User = get_user_model()
            user = User.objects.first()  # ✅ temporary fix for testing
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailView(APIView):
    def get_object(self, id):
        try:
            return Transaction.objects.get(id=id)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Budget views ---

class BudgetListView(APIView):
    def get(self, request):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            User = get_user_model()
            user = User.objects.first()  # ✅ temporary fix for testing
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)