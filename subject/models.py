from django.db import models


class Subject(models.Model):

    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
   

    def __str__(self):
        return self.title
    
    class Meta:
        db_table ='subjects'
