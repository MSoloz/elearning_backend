from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
   

    def __str__(self):
        return self.title
    
    class Meta:
        db_table ='topics'
