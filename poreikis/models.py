from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorijos"

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = "Organizacija"
        verbose_name_plural = "Organizacijos"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Projektas"
        verbose_name_plural = "Projektai"

    def __str__(self):
        return self.name


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    maturity_level = models.PositiveSmallIntegerField(default=0, blank=True)
    organization = models.ForeignKey(Organization, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)

    class Meta:
        verbose_name = "Rinkmena"
        verbose_name_plural = "Rinkmenos"

    def __str__(self):
        return self.name


class Request(models.Model):
    OPENED = 1
    CLOSED = 2
    SPAM = 3
    STATUS_CHOICES = (
        (OPENED, "Atidaryta"),
        (CLOSED, "Uždaryta"),
        (SPAM, "Šlamštas"),
    )

    project_name = models.CharField(max_length=255, verbose_name="Projekto ar idėjos pavadinimas")
    author_email = models.EmailField(blank=True, verbose_name="El. pašto adresas pasiteiravimui (nurodyti nebūtina)")
    description = models.TextField(verbose_name="Projekto ar idėjos ir duomenų poreikio aprašymas")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Sukurta")
    updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Pakeista")
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=OPENED, verbose_name="Būsena")

    project = models.ForeignKey(Project, null=True, blank=True, verbose_name="Projektas")
    datasets = models.ManyToManyField(Dataset, blank=True, verbose_name="Duomenų rinkmenos")

    class Meta:
        verbose_name = "Užklausa"
        verbose_name_plural = "Užklausos"

    def __str__(self):
        return self.project_name
