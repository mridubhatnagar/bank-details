from django.db import models

# Create your models here.
class Bank(models.Model):
	ifsc=models.CharField(max_length=11, null=False, blank=False, primary_key=True)
	bank_id=models.BigIntegerField()
	branch=models.CharField(max_length=74, null=True)
	address=models.CharField(max_length=195)
	city=models.CharField(max_length=50)
	district=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	bank_name=models.CharField(max_length=50)


	class Meta:
		db_table='bank'