# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class District(models.Model):
    Id = models.AutoField(primary_key=True, db_column='DistrictID')
    DistrictCode = models.CharField(max_length=50,db_column='DistrictCode')
    DistrictName = models.CharField(max_length=100,db_column='DistrictName', null=False)
    DivisionId = models.IntegerField(db_column='DivisionID', null=False)

    class Meta:
        managed = True
        db_table = 'district'

    def __str__(self):
        return '{}, {}'.format(self.Id, self.DistrictName)



class RegisteredUser(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    UserName = models.CharField(max_length=255, db_column='UserName')
    Mobile = models.CharField(max_length=255, db_column='Mobile')
    Email = models.CharField(max_length=255, db_column='Email', unique=True)
    IsUsed = models.CharField(max_length=10, db_column='IsUsed', default='N')
    Status = models.CharField(max_length=10, db_column='Status', default='1')
    Remark = models.CharField(max_length=255, db_column='Remark', default='1')
    EntryDate = models.DateTimeField(auto_now_add=True, db_column='EntryDate')
    DistrictId = models.ForeignKey(District, db_column='DistrictId', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'RegisteredUser'

    def __str__(self):
        return '{}, {}'.format(self.Id, self.UserName, self.Mobile, self.Mobile, self.Email)
