from django.db import models
from django.utils.safestring import mark_safe


class Video(models.Model):
    class Meta:
        verbose_name = "Видос"
        verbose_name_plural = "Видосы"

    slug = models.SlugField(unique=True,
                            verbose_name="Типа по-английски",
                            help_text="должен быть уникальным")
    urls = models.URLField(verbose_name="Ссылка")
    title = models.CharField(max_length=150, verbose_name="Назваха")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    description = models.TextField(verbose_name="Описалово",
                                   null=True,
                                   blank=True)
    likes = models.PositiveIntegerField(default=0, verbose_name="Лайкосы")
    def __str__(self):
        return self.title

    @property
    def test(self):
        return f"Property hello {self.title}{self.likes ** 2}"

    @property
    def tv(self):
        return mark_safe(f"<iframe width='128' height='72' src='{self.urls}'></iframe>")



class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(auto_now_add=True)
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comment")




# Create your models here.
