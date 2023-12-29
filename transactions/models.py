from django.db import models
from accounts.models import UserAccount
# Create your models here.
DEPOSIT =1
WITHDRAW=2
LOAN = 3
LOAN_PAID = 4

TRANSACTION_TYPE = (
    (1, 'deposit'),
    (2, 'withdraw'),
    (3, 'Loan'),
    (4, 'Loan paid'),
)


class Transaction(models.Model):
    account = models.ForeignKey( UserAccount, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField( max_digits=12, decimal_places=2)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']
