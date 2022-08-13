from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Başlıq')
    description = models.TextField(max_length=255, verbose_name = 'Məzmun')
    status = models.BooleanField(default = False)
    finishdate = models.DateTimeField(null=True, blank=True, verbose_name = 'son gün') 
    user = models.ForeignKey("auth.User" , on_delete=models.CASCADE, verbose_name = 'İstifadəçi')

    class Meta:
        ordering = ['status']
    def __str__(self):
        return self.title