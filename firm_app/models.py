# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink

class Firm(models.Model):
    name=models.CharField(max_length='400', verbose_name="Название")
    description=models.TextField(verbose_name="Описание", null=True, blank=True )
    logo=models.ImageField(upload_to="images/logo", verbose_name="Логотип", null=True, blank=True)
    slug=models.SlugField(unique=True)

    def __unicode__(self):
        return self.name
    def get_adress(self):
        aa="firms/"+self.slug
        return aa
    @permalink
    def get_absolute_url(self):
        return self.id
    class Meta:
        ordering=["name"]

class Rubric (models.Model):
    name=models.CharField(max_length='100', verbose_name='Наименование')
    parent = models.ForeignKey('self',verbose_name="Родительская рубрика", null=True, blank=True)
    firm = models.ManyToManyField('Firm', null=True, blank=True)

    def __unicode__(self):
        if self.parent:
            return u'%s-%s' % (self.parent, self.name)
        return self.name
    class Meta:
        ordering=['name']
        verbose_name_plural="Рубрики"

class Contact(models.Model):
    name=models.CharField(max_length='300', verbose_name="ФИО", null=True, blank=True)
    tel=models.CharField(max_length='20', verbose_name="Телефон", null=True, blank=True)
    mobile=models.CharField(max_length='11', verbose_name="Мобильный", null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    skype=models.CharField(max_length='50', null=True, blank=True )
    comment=models.TextField(verbose_name="Комментарий", null=True, blank=True)
    firm = models.ManyToManyField('Firm', null=True, blank=True)

    def __unicode__(self):
        if self.name:
            return self.name
        return self.tel

class Adress (models.Model):
    name=models.CharField(max_length='300', verbose_name='Название адреса')
    city=models.CharField(max_length='100', verbose_name='Город', null=True, blank=True)
    street=models.CharField(max_length='100', verbose_name='Улица', null=True, blank=True)
    house=models.CharField(max_length='10', verbose_name='дом', null=True, blank=True)
    office=models.CharField(max_length='10', verbose_name='офис', null=True, blank=True)
    description=models.TextField(verbose_name='Описание', null=True, blank=True)
    firm = models.ManyToManyField('Firm', null=True, blank=True)

    def __unicode__(self):
        return self.name

