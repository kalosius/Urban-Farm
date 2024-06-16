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
    period_of_stay = models.CharField(max_length=20, choices=PERIOD_OF_STAY_CHOICES)

    def __str__(self):
        return self.first_name, self.last_name
    
    class Meta:
        verbose_name_plural = 'farmer one'


class UrbanFarmer(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    # date_of_registration = models.DateTimeField
    # date_of_birth = models.DateField
    activities = models.TextField(max_length=200, validators=[MinLengthValidator(20)])
    contact = models.CharField(max_length=15, validators=[MinLengthValidator(10)])
    nin = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    ward = models.ForeignKey(UrbanWard, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    unique_id = models.CharField(max_length=5)
    
    

    def __str__(self):
        return self.first_name, self.last_name
    


class Product(models.Model):
    # Mode of payment
    CASH = 'Cash'
    MOBILE_MONEY = 'Mobile Money'

    PAYMENT_CHOICES = [
        (CASH, 'Cash'),
        (MOBILE_MONEY, 'Mobile Money'),   
    ]

    # Mode of delivery
    PICK_UP = 'Pick up'
    HOME_DELIVERY = 'Home Delivery'

    DELIVERY_CHOICES = [
        (PICK_UP, 'Pick up'),
        (HOME_DELIVERY, 'Home Delivery'),   
    ]

    # PRODUCE TYPE
    ORGANIC = 'Organic'
    NONE_ORGANIC = 'None Organic'

    PRODUCE_TYPE_CHOICES = [
        (ORGANIC, 'Organic'),
        (NONE_ORGANIC, 'None Organic'),   
    ]


    product_name = models.CharField(max_length=30)
    ward_name = models.ForeignKey(UrbanWard, on_delete=models.CASCADE)
    # date = models.date
    unit_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    mode_of_payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    address = models.CharField(max_length=30)
    mode_of_delivery = models.CharField(max_length=40, choices=DELIVERY_CHOICES)
    produce_type = models.CharField(max_length=20, choices=PRODUCE_TYPE_CHOICES)

    def __str__(self):
        return self.product_name



    


