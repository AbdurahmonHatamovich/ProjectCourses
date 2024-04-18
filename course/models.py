from django.db import models

class Speciality(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course/speciality/')
    create_date = models.DateTimeField(auto_now=True)
    last_update_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"

class Course(models.Model):
    class PriceType(models.TextChoices):
        USD = "USD", "$"
        UZS = "UZS", "sum"
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course/course/')
    description = models.TextField()
    active_users = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    price_type = models.CharField(max_length=20, choices=PriceType.choices,default=PriceType.UZS)
    rating = models.FloatField(default=0)
    speciality = models.ManyToManyField(Speciality)
    create_date = models.DateTimeField(auto_now=True)
    last_update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Position(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)
    last_update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course/teacher/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    t_link = models.URLField(null=True, blank=False)
    f_link = models.URLField(null=True, blank=False)
    l_link = models.URLField(null=True, blank=False)
    create_date = models.DateTimeField(auto_now=True)
    last_update_date = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
