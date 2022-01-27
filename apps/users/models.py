# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    userid = models.IntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=1)  # Field name made lowercase.
    userno = models.CharField(db_column='userNo', max_length=30)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=30)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=255)  # Field name made lowercase.
    userstatus = models.CharField(db_column='userStatus', max_length=1)  # Field name made lowercase.
    usercreatetime = models.DateTimeField(db_column='userCreatetime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
