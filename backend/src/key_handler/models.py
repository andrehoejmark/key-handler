from django.db import models
from django.utils import timezone

# Create your models here
class Key(models.Model):
    
    
    license = models.CharField(max_length=200, primary_key=True)
    num_sessions_allowed = models.IntegerField(default=1)
    expire_date = models.DateTimeField(default=None, blank=True, null=True)

    TYPE_CHOICES = [('Monthly',1), ('Third Month', 2), ('Yearly', 3)]
    sub_type = models.CharField(choices=TYPE_CHOICES, default='1', max_length=100)

class Session(models.Model):
    remote_session_id = models.CharField(default="0", max_length=200)
    license = models.ForeignKey(Key, on_delete=models.CASCADE)
    expire_date = models.DateTimeField(default=timezone.datetime.now()+timezone.timedelta(minutes=5))


class User(models.Model):
    email = models.ForeignKey(Key, on_delete=models.CASCADE) # on making this oncasacde delete because it could be good information if someone wants to look up something and oh I know my old key..
    


