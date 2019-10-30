from django.db import models

class Vehicle(models.Model):
    """
    harusnya dibagi merek dan type
    """
    nama = models.fields.CharField(max_length=255)
    harga = models.fields.FloatField()

    def __str__(self):
        return self.nama

    def __repr__(self):
        return self.nama


JK = (('L','Laki-Laki'),
      ('P','Perempuan'),)
OCCUPATION = (('N','NON-FIX'),
              ('F','FIX'),)


# Create your models here.
class Customer(models.Model):
    nama = models.fields.CharField(max_length=255)
    jk = models.fields.CharField(max_length=1, choices=JK, default='L')
    gaji = models.fields.FloatField()
    existing = models.fields.BooleanField()
    occupation = models.fields.CharField(max_length=5, choices=OCCUPATION, default='F')
    alamat = models.fields.TextField()
    kendaraan = models.ManyToManyField(Vehicle)

    def __str__(self):
        return self.nama

    def __repr__(self):
        return self.nama

