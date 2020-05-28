from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    LEVELS = (
        ('J', 'Junior deweloper'),
        ('M', 'Middle deweloper'),
        ('S', 'Senior deweloper'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    level = models.CharField(max_length=1, choices=LEVELS, default='J')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
