from django.db import models

class Payment(models.Model):
    student_name = models.CharField(max_length=100)
    student_ID = models.CharField(max_length=50, default="")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=50, default="")
    year = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.student_name} - ${self.amount_paid}'
