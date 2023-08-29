from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='images/')
    video_path = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table ='courses'
