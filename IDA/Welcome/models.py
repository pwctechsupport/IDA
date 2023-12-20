# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class WelcomeUserlogin(models.Model):
    userloginid = models.AutoField(db_column='UserLoginID', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username')  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LastLogin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WelcomeUserLogin'

class WelcomeLoginAttempt(models.Model):
    loginattemptid = models.AutoField(db_column='LoginAttemptID', primary_key=True)
    username = models.TextField(db_column='Username')
    count = models.IntegerField(db_column='Count')
    lastattempt = models.DateTimeField(db_column='LastAttempt')
