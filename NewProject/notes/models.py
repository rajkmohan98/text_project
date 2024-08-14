from django.db import models

# Create your models here.


class Notes_table(models.Model):
    user_name=models.CharField(max_length=50)
    text_content=models.TextField(max_length=3000)