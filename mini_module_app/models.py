from django.db import models
import os

class Files(models.Model):

    subjects = (('Парадигмы', 'Парадигмы',), ('Копьютерные сети', 'Копьютерные сети',), ('Человек и компьютер', 'Человек и компьютер',)
                , ('Проектирование програмных систем', 'Проектирование програмных систем',), ('Педагогика и Психология', 'Педагогика и Психология',))
    types = (('Лекция', 'Лекция',), ('Практика', 'Практика',), ('Лабораторная', 'Лабораторная',))

    subject = models.CharField(max_length=50, verbose_name='Предмет', choices=subjects)
    type = models.CharField(max_length=50, verbose_name='Тип', choices=types)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    file = models.FileField(verbose_name='Файл', upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def path(self):
        return self.file.path

    @property
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def name(self):
        return self.subject + ' - ' + self.title


    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-title']


class Calendar(models.Model):
    title = models.CharField(max_length=10, verbose_name='Заголовок')
    note = models.CharField(max_length=250, verbose_name='Заметка')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Facts(models.Model):
    text = models.TextField()
