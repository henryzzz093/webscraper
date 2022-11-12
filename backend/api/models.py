from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Apartments(BaseModel):
    company = models.CharField(max_length=30)
    date = models.DateField(auto_now=True, null=True, blank=True)
    floorplan = models.CharField(max_length=30, null=True, blank=True)
    available = models.CharField(max_length=100, null=True, blank=True)
    bedrooms = models.CharField(max_length=100, null=True, blank=True)
    baths = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    deposit = models.CharField(max_length=100, null=True, blank=True)
    rent = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.floorplan

    class Meta:
        verbose_name_plural = "Apartments"