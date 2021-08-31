from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.urls import reverse

from users.models import Profile


class Car(models.Model):
    BRAND_SAIPA = 1
    BRAND_IRAN_KHODRO = 2
    BRAND_HYUNDAI = 3
    BRAND_CHOICES = [
        (BRAND_SAIPA, 'Saipa'),
        (BRAND_IRAN_KHODRO, 'Iran Khodro'),
        (BRAND_HYUNDAI, 'Hyundai'),
    ]

    brand = models.PositiveSmallIntegerField(_('Brand'),
                                             choices=BRAND_CHOICES,
                                             default=BRAND_SAIPA)
    name = models.SlugField(_('Name'))
    color = models.CharField(_('Color'), max_length=10, blank=True)
    price = models.IntegerField(_('Price'),
                                help_text=_('In Tomans'),
                                validators=(MinValueValidator(10_000_000), ))
    is_enable = models.BooleanField(_('Is Enable'), default=True)

    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rent:car_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')
        unique_together = (('brand', 'name'), )


class CarRent(models.Model):
    user = models.ForeignKey(Profile,
                             verbose_name=_('user'),
                             on_delete=models.CASCADE)
    car = models.ForeignKey(Car,
                            verbose_name=_('car'),
                            on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(_('amount'))
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_enable = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('car rent')
        verbose_name_plural = _('car rents')

    def __str__(self):
        return f'{self.user}, car: {self.car}, amount: {self.amount}'
