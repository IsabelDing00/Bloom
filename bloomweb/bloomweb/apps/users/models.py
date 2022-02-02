from django.db import models


# The first virsion: if we build all the tables under one app: users.


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=255)
    company_name = models.CharField(max_length=225, blank=True, null=True)
    email = models.EmailField(blank=False,unique=True)
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_zip_code = models.CharField(max_length=50)
    user_address = models.TextField()
    campaign_info = models.TextField()
    template_info = models.TextField()
    campaign_list = models.TextField()
    templates = models.TextField()
    global_templates = models.TextField()

class Campaign(models.Model):
    campaign_name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    contact_table = models.ForeignKey("CampaignContact", on_delete=models.CASCADE)
    campaign_status = models.CharField(max_length=10)
    campaign_template = models.ForeignKey("CampaignTemplate", on_delete=models.CASCADE)
    campaign_date = models.DateField(auto_now_add=True)
    campaign_metric = models.CharField(max_length=50,blank=True)

class CampaignContact(models.Model):
    campaign_id = models.ForeignKey("Campaign", on_delete=models.CASCADE)
    global_contact = models.ForeignKey("GlobalContact", on_delete=models.CASCADE)

class CampaignTemplate(models.Model):
    campaign_template_id = models.AutoField(primary_key=True)
    campaign_id = models.CharField(max_length=50)
    global_template_id = models.IntegerField()

class Metrics(models.Model):
    campaign_template = models.OneToOneField("CampaignTemplate", on_delete=models.CASCADE)
    email_sent = models.IntegerField()
    email_opened = models.IntegerField()
    email_bounced = models.IntegerField()
    # Add more based on sendgrid data

class GlobalContact(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.TextField()
    email = models.EmailField(blank=False)
    gender = models.CharField(max_length=2, blank=True, null=True)
    contact_status = models.CharField(max_length=10)
    campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE)
    template = models.ForeignKey("CampaignTemplate", on_delete=models.CASCADE)
    is_spammer = models.CharField(max_length=1, blank=True, default='N')
    last_time_contact = models.DateField(auto_now_add=True)
    x_time_contact = models.IntegerField()
    activity = models.TextField()
    upload_list_id = models.ForeignKey("UploadList", on_delete=models.CASCADE)

class UploadList(models.Model):
    upload_list_id = models.AutoField(primary_key=True)
    date_create = models.DateField(blank=False)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

class GlobalTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    template_version = models.IntegerField(blank=True, default='0')
    message = models.TextField(blank=True)




