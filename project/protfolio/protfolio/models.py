from django.db import models

class About(models.Model):
    u_name = models.CharField(max_length=500)
    dob = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    no_exp = models.CharField(max_length=500)
    no_happy_customers = models.CharField(max_length=500)
    no_project_finished = models.CharField(max_length=500)
    no_digital_awards = models.CharField(max_length=500)
    discription = models.TextField(max_length=500)
    date_time = models.CharField(max_length=500)


class companies(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="image/")

       
 