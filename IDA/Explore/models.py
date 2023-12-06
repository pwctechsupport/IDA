from django.db import models

# Create your models here.

class Chatlist(models.Model):
    chatlistid = models.AutoField(primary_key=True)
    chatlistcode = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isquestion = models.IntegerField(blank=True, null=True)
    parentchatcode = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.
    isreset = models.IntegerField(blank=True, null=True)
    isupload = models.IntegerField(blank=True, null=True)
    mltype = models.TextField(blank=True, null=True)
    issample = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chatlist'
