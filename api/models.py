from django.contrib.auth.models import User
from django.db import models

class Categories(models.Model):
    name = models.TextField(blank=True,default='')

    def __str__(self):
        return self.name

class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='unknown')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Categories,related_name='categories',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket,related_name='tickets',on_delete=models.CASCADE)

    def __str__(self):
        return self.body





