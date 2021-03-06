from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User,
                                verbose_name=_('user'),
                                on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(_('age'))
    avatar = models.ImageField(_('avatar'),
                               upload_to='users',
                               blank=True,
                               null=True)
    phone_number = models.PositiveBigIntegerField(
        _('phone number'),
        unique=True,
    )
    bio = models.TextField(_('bio'), blank=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return reverse('users:profile_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'id: {self.user.id} phone: {self.phone_number}'
