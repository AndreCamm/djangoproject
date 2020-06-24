from django.db import models

safety_level = (
    ('SAFE', 'Safe'),
    ('EUCLID', 'Euclid'),
    ('KETER', 'Keter'),
)

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Monster(models.Model):
    monster_name = models.CharField(max_length=50)
    behaviour_type = models.CharField(choices=safety_level, max_length=6)
    image = models.ImageField(upload_to ='uploads/', default='./uploads/default.png')
    description = models.TextField()
    monster_location = models.ManyToManyField(Location)

    def __str__(self):
        return self.monster_name