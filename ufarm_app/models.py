from django.db import models
from django.core.validators import MinLengthValidator


# Urban Ward Model(LCs)
class UrbanWard(models.Model):
    MPERERWE = 'Mpererwe'
    KASANGATI = 'Kasangati'
    GAYAZA = 'Gayaza'
    WAMPEWO = 'Wampewo'

    WARD_CHOICES = [
        (MPERERWE, 'Mpererwe'),
        (KASANGATI, 'Kasangati'),
        (GAYAZA, 'Gayaza'),
        (WAMPEWO, 'Wampewo'),
    ]

    name = models.CharField(max_length=50, choices=WARD_CHOICES)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'urban ward'


class FarmerOne(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    ward = models.ForeignKey(UrbanWard, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name
    
    class Meta:
        verbose_name_plural = 'farmer one'


class UrbanFarmer(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    farmer_one = models.ForeignKey(FarmerOne, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name
    
    


