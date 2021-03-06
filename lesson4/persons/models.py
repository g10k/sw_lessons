# coding=utf-8
from django.db import models
from django.core import validators
# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    birth = models.DateField(u'Дата рождения', blank=True, null=True)
    email = models.EmailField(u'Почта', null=True)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def fio_upper(self):
        return unicode(self).upper()


class Passport(models.Model):
    serial = models.PositiveIntegerField(validators=[validators.MaxValueValidator(9999)])
    number = models.PositiveIntegerField(validators=[validators.MaxValueValidator(999999)])
    person = models.OneToOneField('Person', on_delete=models.CASCADE, null=True, blank=True, related_name='passport')
    propiska = models.TextField(u'Прописка')

    def __unicode__(self):
        return '%s %s' % (self.serial, self.number)

    class Meta:
        unique_together = ('serial','number')


# Количество людей в БД
    # Person.objects.count() или len(Person.objects.all())

# Рожденные после 1995 года.
    # import datetime
    # year_1995 = datetime.date(year=1995,month=12,day=31)
    # Person.objects.filter(birth__gt=year_1995)
    # или
    # Person.objects.filter(birth__year__gt=1995) # Но не в sqlite, а mysql и др.

#  Первый человек по алфавитному порядку
    # Person.objects.order_by('last_name')[0]

# Исключить записи у которых нет email
    # Person.objects.exclude(email__isnull=True)