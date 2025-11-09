from django.db import models

class Author(models.Model):
    name = models.CharField('имя',max_length=64)
    surname = models.CharField('фамилия',max_length=64)
    patronimyc = models.CharField('отчество', max_length=64)

    birth_date = models.DateField('дата рож')
    death_date = models.DateField('дата см',null=True,blank=True)

    def __str__(self):
        return f'{self.name},{self.surname},{self.patronimyc}'
    class Meta:
        verbose_name ='author'
class Book(models.Model):
    name = models.CharField(max_length=128,verbose_name='название')
    author=models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name='автор')
    about=models.TextField(verbose_name='описание',help_text='напиши о книге')
    price = models.FloatField(verbose_name='цена',default=5)
    count=models.IntegerField(verbose_name='кол',default=5)

    TYPES = (
        ('такие есть',(
            ('t','твёрдый'),
            ('m','мягкий'),
        )),
        ('а таких может не быть',(
            ('s','средний'),
        ))
    )
    pereplet = models.CharField('переплёт', max_length=1,choices=TYPES,default='t')

    def __str__(self):
        return f'{self.name},{self.author}'