from django.db import models


class Project(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    main_img = models.ImageField('Главное изображение', upload_to='img/project')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Form (models.Model):
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    description = models.CharField('Описание заявки', max_length=300)
    email = models.EmailField('Почта', max_length=150, blank=True)
    number = models.CharField('Номер телефона', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формы заявки'
        verbose_name_plural = 'Форма заявки'

