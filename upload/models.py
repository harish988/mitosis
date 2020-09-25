from django.db import models

class Model(models.Model):
    id = models.IntegerField(unique=True, blank=False, null=False, primary_key=True)
    model = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.model


class Upload(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name