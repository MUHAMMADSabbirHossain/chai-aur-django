from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPES_CHOICES = [
        ('ML', "MASALA"),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to  = 'chais/')
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length = 2, choices = CHAI_TYPES_CHOICES)
    description = models.TextField(default = '')
    price = models.TextField(default = 0)

    def __str__(self):
        return self.name
