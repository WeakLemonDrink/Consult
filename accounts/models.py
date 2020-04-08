from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Organisation(models.Model):
    org_name = models.CharField(max_length=100, blank=True, null=True)
    org_id = models.CharField(max_length=5, blank=True, null=True)
    
    class Meta:
        ordering = ["org_name"]

    def __str__(self):
        return self.org_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alt_id = models.CharField(max_length=5, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)
    house_name_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=100, blank=True, null=True)
    gdpr_consent = models.BooleanField(default=False)
    
    def __str__(self):  
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save() 
    
    
class Client(models.Model):
    client_first_name = models.CharField(max_length=100, blank=True, null=True)
    client_last_name = models.CharField(max_length=100, blank=True, null=True)
    client_org = models.CharField(max_length=100, blank=True, null=True)
    client_email = models.EmailField(max_length=254, blank=True, null=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.client_last_name + ", " + self.client_first_name

