from django.db import models


# Create your models here.
class list_of_accounts(models.Model):
    account_id = models.CharField(max_length=10, null=True)
    quantity_cat_point = models.IntegerField(null=True)