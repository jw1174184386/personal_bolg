from django.db import models
from django.utils import timezone

"""
    出版社表
"""


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='出版社')
    address = models.CharField(max_length=100, verbose_name='出版社地址')
    city = models.CharField(max_length=60, verbose_name='出版城市')
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name
        ordering = ["-name"]

    def __str__(self):
        return self.name


"""
    作者表
"""


class Author(models.Model):
    salutation = models.CharField(verbose_name='称呼', max_length=10)
    name = models.CharField(verbose_name='姓名', max_length=200)
    sex_choices = (('0', '女'), ('1', '男'))
    sex = models.CharField(verbose_name='性别', max_length=2, choices=sex_choices, default='男')
    email = models.EmailField(verbose_name="电子邮箱")

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.salutation


"""
    书籍表
"""


class Book(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    authors = models.ManyToManyField(Author)
    information = models.TextField(verbose_name='主题介绍', max_length=1000)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(verbose_name='发布时间', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['-publication_date']

    def __str__(self):
        return self.title
