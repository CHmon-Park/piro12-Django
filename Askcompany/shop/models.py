from django.db import models
from askcompany.utils import uuid_upload_to
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank = True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.name}'

    class Meta:
        ordering = ['id']       # -id 이면 역순순

    def get_absolute_url(self):
        return reverse("shop:item_detail", args=[self.pk])
        # return reverse('shop:item_datil', kwargs={'pk':self.pk}}