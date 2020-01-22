# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DailyDatabase(models.Model):
    serial_number = models.IntegerField(db_column='Serial_Number')  # Field name made lowercase.
    site_name = models.CharField(db_column='Site_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organisation = models.CharField(db_column='Organisation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tender_id = models.CharField(db_column='Tender_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publish_date = models.CharField(db_column='Publish_Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deadline = models.CharField(db_column='Deadline', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tender_amount = models.CharField(db_column='Tender_Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emd_amount = models.CharField(db_column='EMD_Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tender_link = models.TextField(db_column='Tender_Link', blank=True, null=True)  # Field name made lowercase.
    tender_details = models.TextField(db_column='Tender_Details', blank=True, null=True)  # Field name made lowercase.
    upload_date = models.DateField(db_column='Upload_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daily_database'


class MasterDatabase(models.Model):
    serial_number = models.IntegerField(db_column='Serial_Number')  # Field name made lowercase.
    site_name = models.CharField(db_column='Site_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organisation = models.CharField(db_column='Organisation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tender_id = models.CharField(db_column='Tender_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publish_date = models.CharField(db_column='Publish_Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deadline = models.CharField(db_column='Deadline', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tender_amount = models.CharField(db_column='Tender_Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emd_amount = models.CharField(db_column='EMD_Amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tender_link = models.TextField(db_column='Tender_Link', blank=True, null=True)  # Field name made lowercase.
    tender_details = models.TextField(db_column='Tender_Details', blank=True, null=True)  # Field name made lowercase.
    upload_date = models.DateField(db_column='Upload_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'master_database'
