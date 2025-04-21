from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    type=models.CharField(max_length=30)


class police_station(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    pin=models.IntegerField()
    post=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    langtitude=models.FloatField()
    longtitude=models.FloatField()


class users_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    pin=models.IntegerField()
    post=models.CharField(max_length=30)




class complaint_table(models.Model):
    USER =models.ForeignKey(users_table,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=30)
    replay=models.CharField(max_length=30)
    date=models.DateField()

class camera_table(models.Model):
        camera_number = models.IntegerField()
        latitude = models.FloatField()
        longitude = models.FloatField()


class report_table(models.Model):
    USER = models.ForeignKey(users_table, on_delete=models.CASCADE)
    CAM_ID =models.ForeignKey(camera_table,on_delete=models.CASCADE)
    report=models.CharField(max_length=30)
    visitorlogid=models.IntegerField()
    date=models.DateField()
    place=models.CharField(max_length=30)
    time=models.TimeField()


class familiarperson_table(models.Model):
    USERID=models.ForeignKey(users_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    relation=models.CharField(max_length=30)
    image=models.FileField()
    date=models.DateField()

class visitor_table(models.Model):
    visitorid=models.IntegerField()
    familiarperson=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    type=models.CharField(max_length=30)

class alert_table(models.Model):
    camera=models.CharField(max_length=30)
    image=models.FileField()
    data=models.CharField(max_length=30)
    type=models.CharField(max_length=30)




class alertreport_table(models.Model):
    ALERTID=models.ForeignKey(alert_table,on_delete=models.CASCADE)
    date=models.DateField()
    state=models.CharField(max_length=30)
    police=models.CharField(max_length=30)

