from django.db import models

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