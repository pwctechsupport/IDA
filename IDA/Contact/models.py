from django.db import models

# Create your models here.
class Contactus(models.Model):
    contactusid = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    submittime = models.DateTimeField(db_column='SubmitTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contactus'
