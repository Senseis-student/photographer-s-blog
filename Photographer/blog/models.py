from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    text = models.TextField()
    data = models.DateField(auto_now=True)
    img = models.ImageField('Изображение', blank=True, upload_to='blog/')

    def __str__(self): 
        return self.title

    class Meta:
        verbose_name = 'Статья' 
        verbose_name_plural = 'Статьи' 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)#означает что если удалить пост комментарии тоже удалятся
    author = models.TextField('Автор', blank=False)
    textComment = models.TextField('Текст комментария', blank=False)
    
    def __str__(self):
        return f'Комментарий от {self.author} для {self.post}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
