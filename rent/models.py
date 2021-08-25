from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


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

    class Meta:
        ordering = ('id', )
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')
        unique_together = (('brand', 'name'), )
