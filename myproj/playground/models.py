from django.db import models
from django.db.models.signals import post_save
from datetime import timedelta
from django.utils import timezone

UNIVERSITY_DOMAIN = 'ourdomain.edu'

class Student(models.Model):

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class StudentInfo(models.Model):
    class Meta:
        verbose_name = "StudentInfo"
        verbose_name_plural = "StudentInfos"

    email = models.EmailField(unique=True)
    pass_id = models.CharField(max_length=10, null=True, unique=True)
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key = True,
        related_name = 'info',
    )

    def __str__(self):
        return f'{self.pass_id}'

def create_student_info(instance, created, **kwargs):
    if not created:
        return
    count = Student.objects.filter(first_name=instance.first_name).count()
    new_email = f'{instance.first_name.lower()}{count}@{UNIVERSITY_DOMAIN}'
    StudentInfo.objects.create(student=instance, email=new_email)
    
post_save.connect(create_student_info, sender=Student)


#

class Publisher(models.Model):
    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    title = models.CharField(max_length=250)
    #body = models.TextField()
    pub_date = models.DateField()
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
    )

    @property
    def added_recently(self):
        return self.pub_date > timezone.localdate() - timedelta(days=1)

    def __str__(self):
        return f'{self.title} on {self.pub_date}'

#

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label



class Shop(models.Model):
    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
    

    title = models.CharField(max_length=100)
    #address
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
