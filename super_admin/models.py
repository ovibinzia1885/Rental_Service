from django.db import models


class VehicleType(models.Model):
    name = models.CharField(max_length=200, verbose_name='Vehicle Type')

    def __str__(self):
        return str(self.name)


class From(models.Model):
    from_name = models.CharField(max_length=200, verbose_name='From ')

    def __str__(self):
        return str(self.from_name)


class To(models.Model):
    to_name = models.CharField(max_length=200, verbose_name='To ')

    def __str__(self):
        return str(self.to_name)


class Distance(models.Model):
    location_from = models.ForeignKey(From, on_delete=models.CASCADE)
    location_to = models.ForeignKey(To, on_delete=models.CASCADE)
    distance = models.CharField(max_length=5, verbose_name='Distance in KM')

    def __str__(self):
        return str(self.location_from)
