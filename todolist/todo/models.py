from django.db import models
from datetime import datetime


# Create your models here.
class List_model(models.Model):
    username=models.CharField(max_length=50)
    work=models.TextField()
    setting_date=models.DateField(null = True)
    #default=datetime.date.today()
    setting_time=models.TimeField(null = True)
#     now = datetime.now()       default=datetime.now().strftime("%H:%M:%S")

# current_time = now.strftime("%H:%M:%S")
    work_status=models.BooleanField(default=False)

    def __str__(self):
        return self.username
