from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        db_table = 'person_data'

    def __str__(self):
        return f"{self.name} ({self.age})"