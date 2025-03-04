from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]

    EDUCATION_CHOICES = [
        ('secondary', 'Среднее'),
        ('higher', 'Высшее'),
        ('postgraduate', 'Послевузовское'),
        ('other', 'Другое'),
    ]

    STRESS_LEVEL_CHOICES = [(i, str(i)) for i in range(1, 11)]

    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Пол")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона (по желанию)")
    city = models.CharField(max_length=100, verbose_name="Город")
    country = models.CharField(max_length=100, verbose_name="Страна")
    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES, verbose_name="Уровень образования")
    other_education = models.CharField(max_length=100, blank=True, null=True, verbose_name="Другое образование")
    profession = models.CharField(max_length=100, verbose_name="Ваша профессия")
    workplace = models.CharField(max_length=100, blank=True, null=True, verbose_name="Место работы (по желанию)")
    smokes = models.BooleanField(default=False, verbose_name="Курите ли вы?")
    drinks_alcohol = models.BooleanField(default=False, verbose_name="Употребляете ли вы алкоголь?")
    stress_level = models.IntegerField(choices=STRESS_LEVEL_CHOICES, verbose_name="Уровень стресса")
    goals = models.CharField(max_length=100, blank=True, null=True, verbose_name="Цели регистрации")
    consent = models.BooleanField(default=False, verbose_name="Согласие на обработку данных")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    additional_comments = models.TextField(blank=True, null=True, verbose_name="Дополнительные комментарии")


    USERNAME_FIELD = 'email'
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"{self.surname} {self.name}"

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='results', on_delete=models.CASCADE)
    result = models.FloatField(verbose_name="Результат")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"Result {self.result} for {self.user}"