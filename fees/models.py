from django.db import models

# Create your models here.

# class mainFields(models.Model):
#     buying_price = models.FloatField(default=0)
#     silling_price = models.FloatField(default=0)

#     def get_profit(self):
#         ebay_fees = (self.silling_price * 14.4) + 0.35
#         profit = (self.silling_price - ebay_fees) - self.buying_price
#         return profit