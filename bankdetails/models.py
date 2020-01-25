from django.db import models

# Create your models here.
class Bank(models.Model):
	ifsc=models.CharField(max_length=11, null=False, blank=False, primary_key=True)
	bank_id=models.BigIntegerField()
	branch=models.CharField(max_length=74, null=False, blank=False)
	address=models.CharField(max_length=195, null=False, blank=False)
	city=models.CharField(max_length=50, null=False, blank=False)
	district=models.CharField(max_length=50, null=False, blank=False)
	state=models.CharField(max_length=50, null=False, blank=False)
	bank_name=models.CharField(max_length=50, null=False, blank=False)


	class Meta:
		db_table='bank'