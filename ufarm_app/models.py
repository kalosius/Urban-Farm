from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator


# Gender Choices
MALE = 'Male'
FEMALE = 'Female'

GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),   
]

# Residence type
RENT = 'Rent'
OWNER = 'Owner'

RESIDENCE_CHOICES = [
    (RENT, 'Rent'),
    (OWNER, 'Owner'),   
]

# Period of stay
FIVE = '5yrs'
SIX = '6yrs'
SEVEN = '7yrs'
EIGHT = '8yrs'
NINE = '9yrs'
TEN = '10+ yrs'

PERIOD_OF_STAY_CHOICES = [
    (FIVE, '5yrs'),
    (SIX, '6yrs'),   
    (SEVEN, '7yrs'),   
    (EIGHT, '8yrs'),   
    (NINE, '9yrs'),   
    (TEN, '10+ yrs'),   
]



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
    # date_of_registration = models.DateTimeField
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    # date_of_birth = models.DateField
    activities = models.TextField(max_length=200, validators=[MinLengthValidator(20)])
    nin = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    contact = models.CharField(max_length=15, validators=[MinLengthValidator(10)])
    address = models.CharField(max_length=20)
    residence = models.CharField(max_length=6, choices=RESIDENCE_CHOICES)
    period_of_stay = models.CharField(max_length=20, choices=PERIOD_OF_STAY_CHOICES, validators=[])

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
    
    


