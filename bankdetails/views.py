from bankdetails.models import Bank
from bankdetails.serializers import BankSerializer
from rest_framework import generics
from django.db.models import Q
from bankdetails.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated



class BankDetail(generics.RetrieveAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer
	permission_classes = [IsAuthenticated]


class BranchDetail(generics.ListAPIView):
	serializer_class = BankSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		"""
		GET API to fetch all details of branches, given bank name and a city.
		Along with Limit and Offset functionality. 
		"""
		queryset = Bank.objects.all()
		bank_name = self.request.query_params.get('bank_name', None)
		city = self.request.query_params.get('city', None)
		if (bank_name is not None) and (city is not None):
			queryset = queryset.filter(Q(bank_name=bank_name) & Q(city=city))
			return queryset

	pagination_class = LimitOffsetPagination