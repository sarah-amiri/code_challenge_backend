from django.db import models


class BuyingStock(models.Model):
    USER1 = 'USER1'
    USER2 = 'USER2'
    USER_CHOICES = [
        (USER1, 'user1'),
        (USER2, 'user2'),
    ]
    STOCK1 = 'STOCK1'
    STOCK2 = 'STOCK2'
    STOCK3 = 'STOCK3'
    STOCK_CHOICES = [
        (STOCK1, 'stock1'),
        (STOCK2, 'stock2'),
        (STOCK3, 'stock3'),
    ]
    DENY = 'DENY'
    ACCEPTED = 'ACCEPTED'
    STATUS_CHOICES = [
        (DENY, 'Deny'),
        (ACCEPTED, 'Accepted'),
    ]

    user = models.CharField(max_length=100, choices=USER_CHOICES) # TODO: refactor: foreign key to user
    stock = models.CharField(max_length=100, choices=STOCK_CHOICES)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
