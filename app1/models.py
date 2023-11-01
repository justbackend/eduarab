from django.db import models


class Savol(models.Model):
    savol = models.TextField()

    def __str__(self):
        return self.savol[:30]

class Javob(models.Model):
    ism = models.CharField(max_length=150)
    savol = models.ForeignKey(Savol, models.SET_NULL, null=True, blank=True)
    voice = models.FileField(upload_to='voice')

    def __str__(self):
        return self.ism